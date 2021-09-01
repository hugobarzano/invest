from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import StockData, Stock

Stock = Stock()

@registry.register_document
class StockDataDocument(Document):
    stock = fields.ObjectField(properties={
        'name': fields.TextField(),
    })

    class Index:
        name = 'stocks'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = StockData

        fields = [
            'open',
            'date',
        ]

    def get_queryset(self):
        return super(StockDataDocument, self).get_queryset().select_related(
            'stock'
        )
    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, Stock):
            return related_instance.stocks.all()