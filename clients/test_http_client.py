from django.test import TestCase

from .http_client import HttpClient


class ClientTestCase(TestCase):

    def test_client(self):
        print("HTTP client testing")

    def test_get_stock_data(self):
        c = HttpClient("EGS9M9PKVRPCC946")
        status, body = c.get_stock_data("NIO")
        self.assertEqual((len(body) > 0), True)
        time_serie_key = "Time Series (5min)"
        for k in body[time_serie_key]:
            print("{} --- {}".format(k, body[time_serie_key][k]))
