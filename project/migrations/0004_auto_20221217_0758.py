# Generated by Django 3.2.5 on 2022-12-17 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20221217_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='facilities',
            name='mfl_code',
            field=models.IntegerField(default=1, max_length=250, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='facilities',
            name='facilities',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
