from django.contrib import admin

# Register your models here.
from .models import ShortKeys

admin.site.register(ShortKeys)

from .models import Person

admin.site.register(Person)

