# Generated by Django 5.1.4 on 2025-01-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashtags', '0002_alter_product_name_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='hashtags.tag'),
        ),
    ]
