# Generated by Django 3.2.5 on 2023-02-22 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cqi', '0017_auto_20230222_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='close_project',
            name='county_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cqi.county_qi_projects'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='close_project',
            name='hub_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cqi.hub_qi_projects'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='close_project',
            name='program_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cqi.program_qi_projects'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='close_project',
            name='subcounty_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cqi.subcounty_qi_projects'),
            preserve_default=False,
        ),
    ]