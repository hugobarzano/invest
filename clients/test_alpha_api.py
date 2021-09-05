import unittest
from .alpha_client import AlphaClient

ALPHA_API_KEY_DEV = "EGS9M9PKVRPCC946"


class TestAlphaApi(unittest.TestCase):

    def test_nio(self):
        c = AlphaClient(ALPHA_API_KEY_DEV)
        status, docs = c.get_stock_5_min("NIO")
        print(docs[0])
        self.assertEqual(status,200)
        self.assertGreater(len(docs),0)

    def test_unknown(self):
        c = AlphaClient(ALPHA_API_KEY_DEV)
        status, docs = c.get_stock_5_min("NIOXXX")
        self.assertEqual(status, 200)
        self.assertEqual(len(docs), 0)

if __name__ == '__main__':
    unittest.main()
