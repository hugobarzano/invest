import unittest
from invest.stocks.client.client import Client

class MyTestCase(unittest.TestCase):
    def test_client(self):
        c = Client("EGS9M9PKVRPCC946")
        status,body = c.get_stock_data("NIO")
        self.assertEqual((len(body)>0), True)
        time_serie_key="Time Series (5min)"
        for k in body[time_serie_key]:
            print("{} --- {}".format(k,body[time_serie_key][k]))


if __name__ == '__main__':
    unittest.main()
