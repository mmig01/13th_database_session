from django.contrib import admin

# Register your models here.
from .models import Shortkeys

admin.site.register(Shortkeys)

from .models import Person

admin.site.register(Person)