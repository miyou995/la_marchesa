# Generated by Django 3.2.5 on 2021-08-09 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atributes', '0001_initial'),
        ('core', '0012_alter_photos_big_slide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='couleur',
            field=models.ManyToManyField(related_name='couleur', to='atributes.Couleur'),
        ),
    ]