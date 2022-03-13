# Generated by Django 3.2.12 on 2022-03-13 13:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20211220_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date de Création'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour'),
        ),
    ]