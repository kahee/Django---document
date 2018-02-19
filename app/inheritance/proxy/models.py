from django.db import models
from django.db.models.manager import Manager


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    is_block = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_block = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class AdminManager(Manager):
    def get_queryset(self):
        # all
        return super().get_queryset().filter(is_admin=True)


class Admin(User):
    # 속성 값을 덮어씀
    objects = Manager()

    class Meta:
        proxy = True

    def drop(self, user):
        user.delete()


class Staff(Manager):
    class Meta:
        proxy = True

    def __str__(self):
        return f'{self.name} {스태프}'

    @staticmethod
    def block(user):
        user.is_block = True
        user.save()


class StaffManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_staff=True)
