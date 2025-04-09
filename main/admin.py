from django.contrib import admin

# Register your models here.
from .models import ShortKeys
from .models import Person

admin.site.register(ShortKeys)
admin.site.register(Person)