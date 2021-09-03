from django.test import TestCase

from .client import AlphaClient


class ClientTestCase(TestCase):

    def test_client(self):
        print("HTTP client testing")

    def test_get_stock_data(self):
        c = AlphaClient("EGS9M9PKVRPCC946")
        status, body = c.get_stock_data("NIO")
        self.assertEqual((len(body) > 0), True)
        for k in body[c.time_keys.FIVE_MIN.value]:
            print("{} --- {}".format(k, body[c.time_keys.FIVE_MIN.value][k][c.body_keys.OPEN.value]))
