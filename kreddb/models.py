from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

from kreddb.orm_old import *

SAFE_TRANSLATION = str.maketrans(' &+:,/«»³®`×', '----_\\""3R\'x')

# если max_length=253, значит он выставлен автоматически


# NOT USED
# class User(models.Model):
#     ident = models.CharField(unique=True, max_length=253)
#     password = models.CharField(max_length=253, blank=True)
#
#     class Meta:
#         managed = False
#         db_table = 'user'


# NOT USED
# class Email(models.Model):
#     email = models.CharField(unique=True, max_length=253)
#     user = models.ForeignKey(User, db_column='user', blank=True, null=True)
#     verkey = models.CharField(max_length=253, blank=True)
#
#     class Meta:
#         managed = False
#         db_table = 'email'


class Body(models.Model):
    name = models.CharField(unique=True, max_length=253)

    class Meta:
        managed = False
        db_table = 'body'

    def __str__(self):
        return self.name

    @property
    def safe_name(self):
        try:
            return self.bodycustom.safename
        except ObjectDoesNotExist as e:
            model_custom = BodyCustom(body_ptr=self, safename=self.name.translate(SAFE_TRANSLATION))
            model_custom.save_base(raw=True)  # Обход тикета 7623
            return model_custom.safename

    @classmethod
    def get_by_safe_name(cls, safe_name):
        return BodyCustom.objects.get(safename=safe_name).body_ptr


class BodyCustom(Body):
    safename = models.CharField(blank=True, max_length=100, db_index=True)


class Mark(models.Model):
    name = models.CharField(unique=True, max_length=253)
    group_name = models.CharField(max_length=253)
    url = models.CharField(max_length=253)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mark'
        ordering = ['name']

    def __str__(self):
        return self.name

    def filter_url(self):
        try:
            safename = self.markcustom.safename
        except ObjectDoesNotExist as e:
            custom_mark = MarkCustom(mark_ptr=self, safename=self.name.translate(SAFE_TRANSLATION))
            custom_mark.save_base(raw=True)  # Обход тикета 7623
            safename = custom_mark.safename
        return reverse('kreddb:list_car_models', kwargs={'mark': safename})

    @classmethod
    def get_by_name(cls, name):
        return cls.objects.get(name=name)

    @classmethod
    def get_by_safe_name(cls, safe_name):
        return MarkCustom.objects.get(safename=safe_name).mark_ptr


class MarkCustom(Mark):
    safename = models.CharField(blank=True, max_length=100)

    class Meta:
        managed = True


class CarModel(models.Model):
    name = models.CharField(unique=True, max_length=253)
    generation_count = models.CharField(max_length=253, blank=True)
    mark = models.ForeignKey(Mark)
    url = models.CharField(max_length=253)
    bottom_age = models.IntegerField(null=True, blank=True)
    top_age = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'model'

    @property
    def safe_name(self):
        try:
            safename = self.carmodelcustom.safename
        except ObjectDoesNotExist as e:
            custom_car_model = CarModelCustom(carmodel_ptr=self, safename=self.name.translate(SAFE_TRANSLATION))
            custom_car_model.save_base(raw=True)  # Обход тикета 7623
            safename = custom_car_model.safename
        return safename

    def filter_url(self):
        return reverse('kreddb:list_modifications', kwargs={'mark': self.mark.markcustom.safename, 'car_model': self.safe_name})

    @classmethod
    def get_by_name(cls, name, mark):
        return cls.objects.get(name=name, mark=mark)

    @classmethod
    def get_by_safe_name(cls, safe_name, mark):
        return CarModelCustom.objects.get(safename=safe_name, mark=mark).carmodel_ptr


class CarModelCustom(CarModel):
    safename = models.CharField(blank=True, max_length=100, db_index=True)


class Generation(models.Model):
    name = models.CharField(max_length=253)
    cost = models.CharField(max_length=253)
    car_model = models.ForeignKey(CarModel, db_column='model_id')
    mark = models.ForeignKey(Mark)
    url = models.CharField(unique=True, max_length=253)
    generation = models.CharField(max_length=253, blank=True)
    bottom_age = models.IntegerField()
    top_age = models.IntegerField()
    safename = models.CharField(blank=True, max_length=100, db_index=True)

    class Meta:
        db_table = 'generation'
        ordering = ['-bottom_age']

    @property
    def safe_name(self):
        if self.generation and not self.safename:
            self.safename = self.generation.translate(SAFE_TRANSLATION)
            self.save()
        return self.safename

    @property
    def url_kwargs(self):
        url_kwargs = {'mark': self.mark.name, 'car_model': self.car_model.name, 'generation': self.generation, 'body': '-',
                      'engine': '-', 'gear': '-'}
        return url_kwargs

    def get_absolute_url(self):
        return reverse('kreddb:list_modifications', kwargs=self.url_kwargs)

    @classmethod
    def get_for_model(cls, mark, car_model, **kwargs):
        return cls.objects.get(mark=mark, car_model=car_model, **kwargs)

    #
    # @property
    # def generation(self):
    #     if self._generation:
    #         return self._generation
    #     else:
    #         return ' '  # TODO Used in url, hence should be not empty
    #
    # @generation.setter
    # def generation(self, value):
    #     self._generation = value


class Engine(models.Model):
    name = models.CharField(unique=True, max_length=253)

    class Meta:
        managed = False
        db_table = 'engine'

    @property
    def safe_name(self):
        try:
            return self.enginecustom.safename
        except ObjectDoesNotExist as e:
            model_custom = EngineCustom(engine_ptr=self, safename=self.name.translate(SAFE_TRANSLATION))
            model_custom.save_base(raw=True)  # Обход тикета 7623
            return model_custom.safename

    @classmethod
    def get_by_safe_name(cls, safe_name):
        return EngineCustom.objects.get(safename=safe_name).engine_ptr


class EngineCustom(Engine):
    safename = models.CharField(blank=True, max_length=100, db_index=True)


class Gear(GearDB):

    class Meta:
        proxy = True


class Modification(models.Model):
    name = models.CharField(max_length=253)
    url = models.CharField(unique=True, max_length=253)
    gear = models.ForeignKey(GearDB)
    engine = models.ForeignKey(Engine)
    mark = models.ForeignKey(Mark)
    car_model = models.ForeignKey(CarModel, db_column='model_id')
    generation = models.ForeignKey(Generation)
    complects_url = models.CharField(max_length=253, blank=True)
    cost = models.CharField(max_length=253, blank=True, null=True)
    body = models.ForeignKey(Body)
    equipment_name = models.CharField(max_length=253, blank=True)
    safename = models.CharField(blank=True, max_length=100, db_index=True)

    class Meta:
        db_table = 'modification'


    @property
    def safe_name(self):
        if self.equipment_name and not self.safename:
            self.safename = self.equipment_name.translate(SAFE_TRANSLATION)
            self.save()
        return self.safename

    def get_absolute_url(self):
        mod_params = {
            'mark': self.mark.markcustom.safename,
            'car_model': self.car_model.safe_name,
            'generation': self.generation.safe_name,
            'gen_year_start': self.generation.top_age,
            'gen_year_end': self.generation.bottom_age,
            'body': self.body.safe_name,
            'engine': self.engine.safe_name,
            'gear': self.gear.name,
            'modification': self.safe_name,
        }
        if self.cost is None:
            mod_params.update({'mod_id': self.id})
        else:
            mod_params.update({'cost': self.cost})
        try:
            url = reverse('kreddb:view_modification', kwargs=mod_params)
        except Exception as e:
            print(e.__str__())
            url = ''
        return url

    @classmethod
    def get_by_name(cls, name, mark, car_model, generation=None):
        # добавил generation=None, чтобы при ajax запросах его не передавать
        # TODO Но вообще этот метод выглядит небезопасным, легко может вернуть >1 комплектации
        qs_filter = dict(equipment_name=name, mark=mark, car_model=car_model)
        if generation:
            qs_filter.update(dict(generation=generation))
        return cls.objects.get(qs_filter)


class KredModification(Modification):
    tie_braker = models.SmallIntegerField(null=True, blank=True)


class EquipmentDict(models.Model):
    name = models.CharField(max_length=253)
    cost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'equipment_dict'
        unique_together = (('name', 'cost'),)


class EquipmentLk(models.Model):
    equipment_dict = models.ForeignKey(EquipmentDict)
    modification = models.ForeignKey(Modification)

    class Meta:
        managed = False
        db_table = 'equipment_lk'
        unique_together = (('modification', 'equipment_dict'),)


class FeatureDict(models.Model):
    name = models.CharField(max_length=253)
    value = models.CharField(max_length=253)

    class Meta:
        managed = False
        db_table = 'feature_dict'
        unique_together = (('name', 'value'),)


class FeatureLk(models.Model):
    feature_dict = models.ForeignKey(FeatureDict)
    modification = models.ForeignKey(Modification)

    class Meta:
        managed = False
        db_table = 'feature_lk'
        unique_together = (('modification', 'feature_dict'),)