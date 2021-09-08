from clients.alpha_client import AlphaClient
from clients.elastic_client import ElasticClient
from .models import Stock

ALPHA_API_KEY_DEV = "EGS9M9PKVRPCC946"
from apscheduler.schedulers.background import BackgroundScheduler
import logging

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

log = logging.getLogger('apscheduler')


def scheduler(func,**kwargs):
    scheduler = BackgroundScheduler()
    scheduler.add_job(func, 'interval', **kwargs)
    scheduler.start()


# Implement as "singleton" or wherever you like to avoid serialize queryobjects errors
class Collector:
    def __init__(self):
        self.elastic = ElasticClient()
        self.alpha = AlphaClient(ALPHA_API_KEY_DEV)

    def stocks_collector(self):
        stocks = Stock.objects.all()
        for s in stocks:
            status_code, stock_data = self.alpha.get_stock_5_min(s.name)
            if len(stock_data) > 0:
                docs = self.elastic.prepare_bulk_data(s.name, stock_data)
                if len(docs) > 0:
                    self.elastic.client.bulk(docs, index="stock-{}".format(s.name))


NEO = Collector()


def load_stocks():
    log.debug("Wake up NEO!")
    NEO.stocks_collector()
