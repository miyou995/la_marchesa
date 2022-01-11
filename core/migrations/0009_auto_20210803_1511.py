# Generated by Django 3.2.5 on 2021-08-03 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_contactform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='message',
            field=models.TextField(blank=True, null=True, verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='subject',
            field=models.CharField(blank=True, max_length=50, verbose_name='Sujet'),
        ),
    ]