from django.apps import AppConfig
from django.core.management import call_command


class DataIngestionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'data_ingestion'
    

class InMemoryDbConfig(AppConfig):
    name = 'data_ingestion'

    def ready(self):
        call_command('migrate',
                     app_label='data_ingestion',
                     verbosity=1,
                     interactive=False,
                     database='default')
                     
                     

