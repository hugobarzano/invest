from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length=8, primary_key=True)
    long_name = models.CharField(max_length=128)
    created = models.DateTimeField('created')

    def __str__(self):
        return self.name



