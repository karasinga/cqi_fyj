# Generated by Django 3.2.5 on 2023-01-30 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0040_alter_testedchange_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hub', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Hubs',
                'ordering': ['hub'],
            },
        ),
        migrations.AlterField(
            model_name='county_qi_projects',
            name='measurement_status',
            field=models.CharField(choices=[('Started or Ongoing', 'STARTING OR ONGOING'), ('Completed or Closed', 'COMPLETED OR CLOSED'), ('Canceled', 'CANCELED'), ('Not started', 'NOT STARTED'), ('Postponed', 'POSTPONED')], max_length=250),
        ),
        migrations.AlterField(
            model_name='hub_qi_projects',
            name='measurement_status',
            field=models.CharField(choices=[('Started or Ongoing', 'STARTING OR ONGOING'), ('Completed or Closed', 'COMPLETED OR CLOSED'), ('Canceled', 'CANCELED'), ('Not started', 'NOT STARTED'), ('Postponed', 'POSTPONED')], max_length=250),
        ),
        migrations.AlterField(
            model_name='program_qi_projects',
            name='measurement_status',
            field=models.CharField(choices=[('Started or Ongoing', 'STARTING OR ONGOING'), ('Completed or Closed', 'COMPLETED OR CLOSED'), ('Canceled', 'CANCELED'), ('Not started', 'NOT STARTED'), ('Postponed', 'POSTPONED')], max_length=250),
        ),
        migrations.AlterField(
            model_name='qi_projects',
            name='measurement_status',
            field=models.CharField(choices=[('Started or Ongoing', 'STARTING OR ONGOING'), ('Completed-or-Closed', 'COMPLETED OR CLOSED'), ('Canceled', 'CANCELED'), ('Not started', 'NOT STARTED'), ('Postponed', 'POSTPONED')], max_length=250),
        ),
        migrations.AlterField(
            model_name='subcounty_qi_projects',
            name='measurement_status',
            field=models.CharField(choices=[('Started or Ongoing', 'STARTING OR ONGOING'), ('Completed or Closed', 'COMPLETED OR CLOSED'), ('Canceled', 'CANCELED'), ('Not started', 'NOT STARTED'), ('Postponed', 'POSTPONED')], max_length=250),
        ),
        migrations.AddField(
            model_name='sub_counties',
            name='hub',
            field=models.ManyToManyField(to='project.Hub'),
        ),
    ]