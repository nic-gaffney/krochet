from django.apps import AppConfig


class KrochetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'krochet'

    def ready(self):
        import hooks
