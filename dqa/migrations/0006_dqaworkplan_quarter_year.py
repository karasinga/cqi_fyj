# Generated by Django 3.2.5 on 2023-02-14 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dqa', '0005_dqaworkplan_facility_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='dqaworkplan',
            name='quarter_year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dqa.period'),
            preserve_default=False,
        ),
    ]
