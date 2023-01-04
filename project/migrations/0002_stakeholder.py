# Generated by Django 3.2.5 on 2023-01-03 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stakeholder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('contact_info', models.CharField(max_length=200)),
                ('impact', models.TextField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.facilities')),
            ],
        ),
    ]
