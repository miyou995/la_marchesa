# Generated by Django 3.2.10 on 2021-12-21 09:00

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_alter_media_is_big'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='media',
            options={'ordering': [django.db.models.expressions.OrderBy(django.db.models.expressions.F('order'), nulls_last=True)], 'verbose_name': 'Banner', 'verbose_name_plural': 'Banners'},
        ),
        migrations.AlterField(
            model_name='media',
            name='page',
            field=models.CharField(choices=[('HO', 'Home page'), ('AB', 'About page'), ('CN', 'Contact page')], default='HO', max_length=2, verbose_name='page de la photo'),
        ),
    ]