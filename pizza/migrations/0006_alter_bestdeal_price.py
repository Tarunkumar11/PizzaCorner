# Generated by Django 3.2.2 on 2021-05-15 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0005_auto_20210515_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestdeal',
            name='price',
            field=models.IntegerField(verbose_name='Price'),
        ),
    ]
