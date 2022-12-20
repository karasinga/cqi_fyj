# Generated by Django 3.2.5 on 2022-12-20 04:55

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_rename_second_name_qi_managers_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qi_team_members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('designation', models.CharField(max_length=250)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('choose_qi_team_member_level', models.CharField(choices=[('Facility QI team member', 'Facility QI team member'), ('Sub-county QI team member', 'Sub-county QI team member'), ('County QI team member', 'County QI team member'), ('Hub QI team member', 'Hub QI team member'), ('Program QI team member', 'Program QI team member')], max_length=250)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.facilities')),
            ],
            options={
                'verbose_name_plural': 'qi team members',
                'ordering': ['first_name'],
            },
        ),
    ]
