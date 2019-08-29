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
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, default="")
    index = models.ForeignKey(Index, on_delete=models.CASCADE, default="")
    empty = models.BooleanField(default=True)

    def __str__(self):
        return str(self.zone.name) + " " + str(self.index.number) + " " + str(self.empty)
