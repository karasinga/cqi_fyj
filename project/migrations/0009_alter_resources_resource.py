# Generated by Django 3.2.5 on 2022-12-17 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_resources_uploaded_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='resource',
            field=models.FileField(default=1, upload_to='resources'),
            preserve_default=False,
        ),
    ]
