from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length=8,primary_key = True)
    long_name = models.CharField(max_length=128)
    created = models.DateTimeField('created')

    def __str__(self):
        return self.name


class StockData(models.Model):
    open = models.CharField(max_length=128)
    date = models.DateTimeField()

    stock = models.ForeignKey(
        Stock,
        related_name='stocks',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.stock.name

    class Meta:
        app_label = 'stocks'
