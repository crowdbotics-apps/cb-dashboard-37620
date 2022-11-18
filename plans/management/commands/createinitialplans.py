from django.core.management.base import BaseCommand, CommandError
from plans.models import Plan

class Command(BaseCommand):

    help = 'Creates the intial Free, Standard and Pro plans'

    def handle(self, *args, **options):
        try:
            if not Plan.objects.filter(name="Free").first():
                Plan.objects.create( name= "Free", description= "This is the free plan", price= 0.0 )

            if not Plan.objects.filter(name="Standard").first():
                Plan.objects.create(name= "Standard", description= "This is the standard plan", price= 10.0 )

            if not Plan.objects.filter(name="Pro").first():
                Plan.objects.create(name= "Pro", description= "This is the standard plan", price= 25.0 )
        except Exception as e:
            raise CommandError("Error creating intial plans: %s" %e)