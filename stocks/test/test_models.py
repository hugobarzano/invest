from django.utils import timezone

from django.test import TestCase
from stocks.models import Stock, StockData
from stocks.documents import StockDataDocument

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

    def test_stockData_model(self):
        my_stock = Stock(
            name="CPS",
            long_name = "CPS TEC",
            created = timezone.now()
        )
        my_stock.save()

        my_stock_data = StockData(
            open = "sss",
            date = timezone.now(),
            stock = my_stock
        )

        my_stock_data.save()
        my_data = StockData.objects.all()

        self.assertEqual(len(my_data), 1)
        self.assertEqual(my_data[0].stock.name,my_stock.name)

    def test_StockDataDocument(self):
        self.test_stockData_model()
        elastic = StockDataDocument().search().execute()

        for d in elastic:
            print(d)