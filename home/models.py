from sre_parse import Verbose
from django.db import models

# Create your models here.
#admin
class University(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=200)

    class Meta:
        verbose_name_plural="Universities"

    def __str__(self):
        return self.name