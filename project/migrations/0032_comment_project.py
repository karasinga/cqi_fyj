# Generated by Django 3.2.5 on 2023-01-28 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0031_auto_20230128_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='project.qi_projects'),
            preserve_default=False,
        ),
    ]
