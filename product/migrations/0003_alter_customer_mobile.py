# Generated by Django 4.2.3 on 2023-07-16 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.BigIntegerField(default=0),
        ),
    ]
