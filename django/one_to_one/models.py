from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name


class Restaurant(models.Model):
    # 테이블은 다르지만 place의 pk와 동일하므로, 자기자신의 pk이만 가져오면됨

    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    serves_hot_dog = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name


class Waiter(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the watiter at %s"(self.name, self.restaurant)
