# Generated by Django 3.2.5 on 2022-12-17 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20221217_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facilities',
            name='mfl_code',
            field=models.IntegerField(unique=True),
        ),
    ]