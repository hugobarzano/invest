# import datetime
# import random
#
# import elasticsearch
# import json
#
#
# def main():
#     es = elasticsearch.Elasticsearch()
#
#     now = datetime.datetime.now()
#     num_docs = 20
#
#     setup(es, now, num_docs)
#     query(es, now, num_docs)
#
#
# def setup(es, now, num_docs):
#     docs = []
#     #es.indices.delete("nio")
#     es.indices.put_template(name="timeseries", body={
#         "index_patterns": ["nio"],
#         "settings": {
#             "number_of_shards": 1
#         },
#         "mappings": {
#             "properties": {
#                 "timestamp": {
#                     "type": "date"
#                 },
#                 "open":{
#                     "type":"double"
#                 }
#             }
#         }
#     })
#     print(now)
#
#     for i in range (10):
#         docs.append({"index": {"_index": "nio"}})
#         docs.append(
#             {
#                 "timestamp": (now - datetime.timedelta(minutes=1)),
#                 "open": random.uniform(1.0, 500.00)
#             }
#         )
#     es.bulk(body=docs,index="nio")
#     # force refresh so we can search
#     es.indices.refresh(index="nio")
#
#
# def query(es, now, num_docs):
#     result = es.search(index="nio", body={
#         "query": {
#             "range": {
#                 "timestamp": {
#                     "gte": now - datetime.timedelta(minutes=15),
#                     "lt": now
#                 }
#             }
#         },
#         #"size": num_docs
#     })
#     #print(result)
#     #print("Found %d results." % result["hits"]["total"])
#     # uncomment below to see all results
#     print(json.dumps(result, indent=4, sort_keys=True))
#
#
# if __name__ == '__main__':
#     main()