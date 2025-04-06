from django.db import models

# Create your models here.
class ShortKeys(models.Model):
    key_name = models.TextField()

    def __str__(self):
        return self.key_name
    #migration은 모델 필드나 db스키마 변경이 있을때만 필요