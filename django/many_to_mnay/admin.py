from django.contrib import admin

# Register your models here.
from many_to_mnay.models import Pizza, Topping

admin.site.register(Pizza)
admin.site.register(Topping)