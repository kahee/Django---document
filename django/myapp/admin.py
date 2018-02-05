from django.contrib import admin

# Register your models here.
from myapp.models import Musician, Album, Person

admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Person)