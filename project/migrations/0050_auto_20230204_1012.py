# Generated by Django 3.2.5 on 2023-02-04 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0049_program_qi_projects_triggers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='county_qi_projects',
            old_name='department',
            new_name='departments',
        ),
        migrations.RenameField(
            model_name='hub_qi_projects',
            old_name='department',
            new_name='departments',
        ),
        migrations.RenameField(
            model_name='program_qi_projects',
            old_name='department',
            new_name='departments',
        ),
        migrations.RenameField(
            model_name='subcounty_qi_projects',
            old_name='department',
            new_name='departments',
        ),
    ]