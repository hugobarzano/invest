from typing import Dict, List, Any, Union

import elasticsearch
from constans.constans import *


class ElasticClient:

    def __init__(self):
        self.client = elasticsearch.Elasticsearch(hosts=["localhost:9200", "es:9200"])

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

    @staticmethod
    def prepare_bulk_data(index_name, data):
        docs = []
        for d in data:
            docs.append({"index": {"_index": index_name}})
            docs.append(d)
        return docs
