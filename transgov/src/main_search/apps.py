from django.apps import AppConfig


class MainSearchConfig(AppConfig):
    name = 'main_search'

    def ready(self):
        import main_search.signals
