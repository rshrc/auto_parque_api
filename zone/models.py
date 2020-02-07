from django.db import models

class Slot(models.Model):
    slot_name = models.CharField(max_length=5, default="")
    car_count = models.IntegerField(default=0)

    def __str__(self):
        return self.slot_name

