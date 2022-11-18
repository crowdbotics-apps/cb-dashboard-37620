# Generated by Django 2.2.28 on 2022-11-18 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user_apps.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserApp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(null=True)),
                ('type', models.CharField(choices=user_apps.models.APP_TYPE, max_length=10)),
                ('framework', models.CharField(choices=user_apps.models.APP_FRAMEWORK, max_length=20)),
                ('domain_name', models.CharField(max_length=255, null=True)),
                ('screenshot', models.URLField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
