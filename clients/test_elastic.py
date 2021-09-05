import datetime
import json
import unittest

from .alpha_client import AlphaClient
from .elastic_client import ElasticClient

ALPHA_API_KEY_DEV = "EGS9M9PKVRPCC946"

class TestElastic(unittest.TestCase):

    def test_ingest_nio(self):
        elastic = ElasticClient()
        elastic.setup_index_template()

        c = AlphaClient(ALPHA_API_KEY_DEV)
        status, docs = c.get_stock_5_min("nio")

        data = elastic.prepare_bulk_data("stock-nio", docs)
        elastic.client.bulk(data,index="sock-nio")
        elastic.client.indices.refresh(index="stock-nio")

        result = elastic.client.search(index="stock-nio", body={
            "query": {
                "range": {
                    "timestamp": {
                        # "gte": now - datetime.timedelta(minutes=15),
                        # "gt": datetime.datetime.now()
                        "lt": datetime.datetime.now()
                    }
                }
            },
        })

        print(json.dumps(result, indent=4, sort_keys=True))
        print("Found %d results." % result["hits"]["total"]["value"])


if __name__ == '__main__':
    unittest.main()
