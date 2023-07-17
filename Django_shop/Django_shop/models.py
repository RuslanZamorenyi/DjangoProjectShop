from django.db import models
from django.template.backends import django


class MyModel(django.db.models.Model:
    my_primary_key = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name