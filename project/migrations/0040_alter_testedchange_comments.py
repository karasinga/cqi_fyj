# Generated by Django 3.2.5 on 2023-01-29 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0039_alter_actionplan_constraints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testedchange',
            name='comments',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]