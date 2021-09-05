import time
import unittest
from datetime import datetime
from elasticsearch import Elasticsearch

class TestAlpah(unittest.TestCase):

    def test_client(self):
        es = Elasticsearch("es:9200")
        doc = {
            'long_name': 'NIO',
            'created': datetime.now(),
            "value":1
        }
        res = es.index(index="test-index", id="NIO", body=doc)
        print(res['result'])

        time.sleep(10)
        test_date=datetime.now()
        doc = {
            'value': 2
        }


        res = es.get(index="test-index", id="NIO")
        print(res['_source'])

        es.indices.refresh(index="test-index")

        res = es.search(index="test-index")
        print("Got %d Hits:" % res['hits']['total']['value'])
        for hit in res['hits']['hits']:
            print(hit)
            print("%s" % hit["_source"]["data"])

if __name__ == '__main__':
    unittest.main()