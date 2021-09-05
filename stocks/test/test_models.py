from django.utils import timezone

from django.test import TestCase
from stocks.models import Stock

class AppTestCase(TestCase):

    def test_stocks(self):
        print("Stocks APP testing\n")
        self.assertEqual(True, True)

    def test_stock_model(self):
        my_stock = Stock(
            name="CPS",
            long_name = "CPS TEC",
            created = timezone.now()
        )
        my_stock.save()
        cps = Stock.objects.get(name="CPS")
        self.assertEqual(my_stock,cps)
