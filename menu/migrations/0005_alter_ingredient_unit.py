# Generated by Django 5.1.2 on 2024-11-16 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_ingredienttype_tag_alter_ingredient_unit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('g', 'grams'), ('ml', 'milliliters'), ('pcs', 'pieces')], max_length=20),
        ),
    ]
