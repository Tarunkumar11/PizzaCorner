# Generated by Django 3.2.2 on 2021-05-13 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pasta',
            name='volume',
            field=models.CharField(choices=[('Half', 'Half'), ('Full', 'Full')], default='Half', max_length=10),
            preserve_default=False,
        ),
    ]
