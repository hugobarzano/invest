from typing import Dict, List, Any, Union

import elasticsearch
from constans.constans import *


class ElasticClient:

    def __init__(self):
        self.client = elasticsearch.Elasticsearch(hosts=[
            # "localhost:9200",
            # "es:9200",
            "https://ka2j6key75:giz0hrmd9j@cesarcorp-3411805901.eu-west-1.bonsaisearch.net:443"])

    def setup_index_template(self):
        self.client.indices.put_template(name="stock", body={
            "index_patterns": ["stock-*"],
            "settings": {
                "number_of_shards": 1
            },
            "mappings": {
                "properties": {
                    TIMESTEAMP: {
                        "type": "date"
                    },
                    OPEN: {
                        "type": "double"
                    },
                    CLOSE: {
                        "type": "double"
                    },
                    HIGH: {
                        "type": "double"
                    },
                    LOW: {
                        "type": "double"
                    },
                    VOL: {
                        "type": "double"
                    }
                }
            }
        })

    def ensure_stock_index(self,index_name):
        self.client.indices.create(index=index_name, ignore=400)

    def prepare_bulk_data(self, stock_name, data):
        index_name = "stock-{}".format(stock_name)
        self.ensure_stock_index(index_name)
        docs = []
        for d in data:
            docs.append({"index": {"_index": index_name}})
            docs.append(d)
        return docs
