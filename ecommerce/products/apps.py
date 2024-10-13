from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

class YourAppConfig(AppConfig):
    name = 'your_app_name'

    def ready(self):
        import products.signals