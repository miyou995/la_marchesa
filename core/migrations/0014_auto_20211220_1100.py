# Generated by Django 3.2.10 on 2021-12-20 10:00

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('atributes', '0001_initial'),
        ('core', '0013_alter_product_couleur'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': [django.db.models.expressions.OrderBy(django.db.models.expressions.F('order'), nulls_last=True)], 'verbose_name': 'Catégorie', 'verbose_name_plural': '- Catégories'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='sous_category',
        ),
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='images/categories'),
        ),
        migrations.AddField(
            model_name='category',
            name='level',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='lft',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='ordre'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='core.category'),
        ),
        migrations.AddField(
            model_name='category',
            name='rght',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='core.category', verbose_name='Sous Catégorie'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='couleur',
            field=models.ManyToManyField(related_name='couleurs', to='atributes.Couleur'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pointure',
            field=models.ManyToManyField(blank=True, related_name='pointures', to='atributes.Pointure'),
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
