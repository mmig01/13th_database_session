from django.contrib import admin

# Register your models here.
from .models import ShortKeys
# 모델을 admin에 등록하여 관리할 수 있도록 설정
admin.site.register(ShortKeys)