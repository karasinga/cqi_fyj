# Generated by Django 3.2.5 on 2023-02-14 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dqa', '0003_auto_20230214_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dqaworkplan',
            name='individuals_responsible',
            field=models.TextField(),
        ),
    ]
