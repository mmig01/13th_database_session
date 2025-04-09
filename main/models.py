from django.db import models

class ShortKeys(models.Model):
    key_name = models.TextField()
    
    def __str__(self):
        return self.key_name



