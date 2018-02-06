from django.contrib import admin

# Register your models here.
from foreign.models import Manufacturer, Car, Person, Type, Pokemon
from many_to_many.models import PostLike, User, Post

admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(Person)
admin.site.register(Type)
admin.site.register(Pokemon)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(PostLike)
