# Generated by Django 3.2.5 on 2023-02-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cqi', '0004_alter_qi_projects_process_analysis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseline',
            name='baseline_status',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='rootcauseimages',
            name='root_cause_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
