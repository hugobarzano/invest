from constans.constans import *
from .http_client import HttpClient
from helper.date_format import date_iso

API_DATA = 'www.alphavantage.co'
STOCK_DATA = '/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=5min&apikey={}'

FIVE_MIN = "Time Series (5min)"


class AlphaClient(HttpClient):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.keys = {
            OPEN: "1. open",
            HIGH: "2. high",
            LOW: "3. low",
            CLOSE: "4. close",
            VOL: "5. volume"
        }

    def decoder(self, date, obj):
        doc = {
            TIMESTEAMP: date_iso(date),
            OPEN: float(obj[self.keys[OPEN]]),
            HIGH: float(obj[self.keys[HIGH]]),
            LOW: float(obj[self.keys[LOW]]),
            CLOSE: float(obj[self.keys[CLOSE]]),
            VOL: float(obj[self.keys[VOL]])
        }
        return doc

    def get_stock_from_api(self, stock_name):
        return self.get(API_DATA, STOCK_DATA.format(stock_name, self.api_key))

    def get_stock_5_min(self, stock_name):
        status_code, data = self.get_stock_from_api(stock_name)
        docs = []
        if FIVE_MIN in data:  # Alpah api always return 200 _OK {'Error Message': ....
            for timestamp in data[FIVE_MIN]:
                print("From Alpha API: {} --- {}".format(timestamp, data[FIVE_MIN][timestamp]))
                doc = self.decoder(timestamp, data[FIVE_MIN][timestamp])
                docs.append(doc)
        return status_code, docs
