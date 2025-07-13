import datetime

from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(default='', max_length=20)
    joining_date = models.DateField(default=datetime.date.today)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"