# Generated by Django 3.2.5 on 2021-08-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='used',
            field=models.IntegerField(default=0, verbose_name='Coupons restant'),
        ),
    ]
