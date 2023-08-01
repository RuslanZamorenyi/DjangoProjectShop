from django.db import models


class NameBrand(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()

    def __repr__(self):
        return self.name, self.description, self.price


class Sizes(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    size = models.IntegerField()

    def __repr__(self):
        return self.size


class Colours(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    colour = models.CharField(max_length=100)

    def __repr__(self):
        return self.colour
