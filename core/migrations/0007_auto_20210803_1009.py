# Generated by Django 3.2.5 on 2021-08-03 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_product_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='actif',
            field=models.BooleanField(default=True, verbose_name='actif'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='actif',
            field=models.BooleanField(default=True, verbose_name='actif'),
        ),
    ]
