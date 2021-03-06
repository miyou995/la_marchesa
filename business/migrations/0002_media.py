# Generated by Django 3.2.10 on 2021-12-20 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_slide', models.ImageField(upload_to='images/slides', verbose_name='URL image ')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='Ordre de la photo')),
                ('actif', models.BooleanField(default=False, verbose_name='Active')),
                ('is_big', models.BooleanField(default=False, verbose_name='Grande photo (1920 x 570) / ')),
                ('is_small', models.BooleanField(default=False, verbose_name='Medium photo (720 x 540)')),
                ('page', models.CharField(default='HO', max_length=2, verbose_name='page de la photo')),
            ],
        ),
    ]
