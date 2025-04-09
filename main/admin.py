from django.contrib import admin
from .models import ShortKeys
from .models import Person

# Register your models here.
admin.site.register(ShortKeys)
admin.site.register(Person)