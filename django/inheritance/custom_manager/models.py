from django.db import models

# Create your models here.
from django.db.models import Manager


class CustomManger(Manager):
    pass


class AbstractBase(models.Model):
    objects = CustomManger()

    class Meta:
        abstract = True
