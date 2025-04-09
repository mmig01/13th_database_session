from django.db import models

# Create your models here.
class Shortkeys(models.Model):
    # 단축키 이름을 나타내기 위한 필드
    key_name = models.TextField()

    def __str__(self):
        return self.key_name
    

class Person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return self.last_name