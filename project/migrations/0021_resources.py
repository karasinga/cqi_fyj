# Generated by Django 3.2.5 on 2022-12-15 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0020_remove_department_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(max_length=250)),
                ('resource', models.FileField(blank=True, null=True, upload_to='resources')),
            ],
        ),
    ]
