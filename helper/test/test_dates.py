import unittest
from helper.date_format import date_iso


class TestDateFormat(unittest.TestCase):

    def test_iso_date(self):
        timestamp = '2021-09-03 19:25:00'
        date = date_iso(timestamp)
        print(date)
        self.assertTrue('T' in date)
