from django.contrib import admin

# Register your models here.
from .models import Place, Waiter, Restaurant

admin.site.register(Restaurant)
admin.site.register(Waiter)
admin.site.register(Place)
