from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Item(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)ss',
        #  이 경우, FOOD 만 인식
        # related_query_name='item',
        related_query_name = '%(app_label)s_%(class)s'

    )

    class Meta:
        abstract = True


class Fruit(Item):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Food(Item):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
