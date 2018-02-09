from django.db import models

# Create your models here.
from django.db.models import Manager


class CustomManger(Manager):
    def get_queryset(self):
        print("Custom manager get_queryset")
        return super().get_queryset()


class OtherManager(Manager):
    def get_queryset(self):
        print("Other manager get_queryset")
        return super().get_queryset()


class AbstractBase(models.Model):
    objects = CustomManger()

    class Meta:
        abstract = True


class ChildA(AbstractBase):
    pass


class ChildB(AbstractBase):
    default_manger = OtherManager()


class ExtraMangerModel(models.Model):
    extra_manger = OtherManager()

    class Meta:
        abstract = True


class ChildC(AbstractBase, ExtraMangerModel):
    pass
gi