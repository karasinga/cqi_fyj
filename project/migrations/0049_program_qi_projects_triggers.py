# Generated by Django 3.2.5 on 2023-02-01 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0048_alter_program_qi_projects_program'),
    ]

    operations = [
        migrations.AddField(
            model_name='program_qi_projects',
            name='triggers',
            field=models.ManyToManyField(blank=True, to='project.Trigger'),
        ),
    ]
