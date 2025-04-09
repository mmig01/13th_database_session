from django.contrib import admin

# Register your models here.
from.models import ShortKeys
from.models import person
admin.site.register(ShortKeys)
admin.site.register(person)