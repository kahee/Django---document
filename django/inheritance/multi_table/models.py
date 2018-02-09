from django.db import models


# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f'Place {self.name} | {self.address}'


class Restaurant(Place):
    # onetoone field가 되기 때문에, place에 id를 참조
    # 무언가를 꺼낼때, 속도가 느리다.
    # 최대 2단계만 속도가 느려지기 때문에
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
    # nearby_places = models.ManyToManyField(
    #     Place,
    #     related_query_name='')

    def __str__(self):
        return f'Restaurant {self.name} | {self.address}'


