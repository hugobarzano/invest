#!/usr/bin/python
import http.client
import ssl
import json
from enum import Enum

API_DATA = 'www.alphavantage.co'
STOCK_DATA = '/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=5min&apikey={}'


class Client:

    def __init__(self, crt, key, password):
        self.crt = crt
        self.key = key
        self.password = password

        self.context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        self.context.load_cert_chain(self.crt, self.key, password=self.password)
        self.context.verify_mode = ssl.CERT_NONE
        self.context.check_hostname = False

    def __init__(self, api_key):
        self.api_key = api_key
        self.context = None

    def without_body(self, url, path, verb):
        try:
            conn = http.client.HTTPSConnection(url, port=443, context=self.context)
            conn.request(verb, path)
            response = conn.getresponse()
            print("Status: {} reason: {} \n".format(response.status, response.reason))
            body = json.loads(response.read())
        except Exception as e:
            print(e)
            return -1, None
        conn.close()
        return response.status, body

    def get(self, url, path):
        return self.without_body(url, path, "GET")


class AlphaBodyKey(Enum):
    OPEN = "1. open"
    HIGH = "2. high"
    LOW = "3. low"
    CLOSE = "4. close"
    VOL = "5. volume"

class AlphaTimeKey(Enum):
    FIVE_MIN ="Time Series (5min)"


class AlphaClient(Client):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.body_keys = AlphaBodyKey
        self.time_keys = AlphaTimeKey

    def get_stock_data(self, stock_name):
        return self.get(API_DATA, STOCK_DATA.format(stock_name, self.api_key))
