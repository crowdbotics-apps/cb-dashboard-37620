from django.db import models
from user_apps.models import UserApp
from plans.models import Plan
from users.models import User


# Create your models here.
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(UserApp, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.DO_NOTHING)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
