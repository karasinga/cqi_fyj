# Generated by Django 3.2.5 on 2022-12-15 05:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0021_resources'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='upload_date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='resources',
            name='uploaded_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
