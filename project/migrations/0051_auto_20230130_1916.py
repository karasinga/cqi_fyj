# Generated by Django 3.2.5 on 2023-01-30 16:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0050_auto_20230130_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='sustainmentplan',
            name='accountable',
            field=models.ManyToManyField(related_name='raci_accountable', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sustainmentplan',
            name='consulted',
            field=models.ManyToManyField(related_name='raci_consulted', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sustainmentplan',
            name='informed',
            field=models.ManyToManyField(related_name='raci_informed', to=settings.AUTH_USER_MODEL),
        ),
    ]
