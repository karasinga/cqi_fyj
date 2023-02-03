# Generated by Django 3.2.5 on 2023-02-01 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0044_sustainmentplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Programs',
                'ordering': ['program'],
            },
        ),
        migrations.AlterModelOptions(
            name='resources',
            options={'ordering': ['-upload_date_updated']},
        ),
    ]
