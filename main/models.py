from django.db import models

# Create your models here.
class ShortKeys(models.Model):
    key_name = models.TextField()
    
    def __str__(self):
        return self.key_name

class Person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    
    def __str__(self):
        return self.last_name