import uuid
from datetime import datetime
from django.db import models


class EntryLog(models.Model):
    car_id = models.CharField(max_length=100, default=0)
    entry_time = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now())

    def __str__(self):
        return str(self.car_id) + " " + str(self.entry_time)
