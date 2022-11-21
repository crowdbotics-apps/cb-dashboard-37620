from django.apps import AppConfig
from django.core.management import call_command

class PlansConfig(AppConfig):
    name = 'plans'

    def ready(self):
        # Temporary workaround to create plans
        call_command('createinitialplans')