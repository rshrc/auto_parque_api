from django.db import models


class Zone(models.Model):
    name = models.CharField(max_length=3, default="")

    def __str__(self):
        return self.name


class Index(models.Model):
    number = models.IntegerField(default=0)

    def __str__(self):
        return str(self.number)


class Slot(models.Model):
    zone_name = models.CharField(max_length=3)
    index_number = models.IntegerField(default=0)
    empty = models.BooleanField(default=True)

    def __str__(self):
        return self.zone_name + " " + str(self.index_number)
