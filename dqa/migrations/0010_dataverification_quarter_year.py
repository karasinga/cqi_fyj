# Generated by Django 3.2.5 on 2023-02-09 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dqa', '0009_alter_period_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataverification',
            name='quarter_year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dqa.period'),
            preserve_default=False,
        ),
    ]
