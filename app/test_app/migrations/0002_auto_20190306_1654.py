# Generated by Django 2.1.7 on 2019-03-06 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='citizen_id',
            new_name='citizen',
        ),
    ]