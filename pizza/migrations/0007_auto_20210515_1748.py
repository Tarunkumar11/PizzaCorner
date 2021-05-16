# Generated by Django 3.2.2 on 2021-05-15 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0006_alter_bestdeal_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestdeal',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='bestdeal',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Deal Offer'),
        ),
    ]