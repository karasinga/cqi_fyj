# Generated by Django 3.2.5 on 2022-12-14 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_program_qi_projects'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='county_qi_projects',
            options={'verbose_name_plural': 'QI_Projects_counties'},
        ),
        migrations.AlterModelOptions(
            name='hub_qi_projects',
            options={'verbose_name_plural': 'QI_Projects_hub'},
        ),
        migrations.AlterModelOptions(
            name='program_qi_projects',
            options={'verbose_name_plural': 'QI_Projects_program'},
        ),
        migrations.AddField(
            model_name='department',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
