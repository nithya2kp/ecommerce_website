# Generated by Django 4.2.3 on 2023-07-10 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('description', models.TextField()),
                ('l_description', models.TextField(null=True)),
                ('category', models.CharField(choices=[('MK', 'Makeup'), ('SC', 'Skincare'), ('HC', 'Haircare'), ('TB', 'Tools & Brushes'), ('BS', 'Body & Shower'), ('FR', 'Fragrance')], max_length=2)),
                ('product_image', models.ImageField(upload_to='item')),
            ],
        ),
    ]
