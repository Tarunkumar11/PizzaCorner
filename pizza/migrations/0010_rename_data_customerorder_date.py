# Generated by Django 3.2.2 on 2021-05-16 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0009_customerorder_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerorder',
            old_name='data',
            new_name='date',
        ),
    ]
