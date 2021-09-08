from django.apps import AppConfig

class StocksConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'stocks'

    def ready(self):
        from .tasks import scheduler,load_stocks
        scheduler(load_stocks,hours=16)
