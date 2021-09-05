#!/usr/bin/python
import http.client
import ssl
import json


class HttpClient:

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
