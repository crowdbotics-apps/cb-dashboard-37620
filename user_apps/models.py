from django.db import models
from enum import Enum
from users.models import User

APP_TYPE = [('Web', 'Web'), ('Mobile', 'Mobile')]
APP_FRAMEWORK = [('Django', 'Django'), ('React Native', 'React Native')]


# Create your models here.
class UserApp(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField(null=True)
    type = models.CharField(max_length=10, choices=APP_TYPE)
    framework = models.CharField(max_length=20, choices=APP_FRAMEWORK)
    domain_name = models.CharField(max_length=255, null=True)
    screenshot = models.URLField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' : ' + (self.domain_name or "")
