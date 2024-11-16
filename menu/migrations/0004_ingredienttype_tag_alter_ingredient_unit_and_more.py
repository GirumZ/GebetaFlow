# Generated by Django 5.1.2 on 2024-11-16 16:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_ingredient_quantity_in_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('g', 'grams'), ('kg', 'kilograms'), ('ml', 'milliliters'), ('l', 'liter'), ('pcs', 'pieces')], max_length=20),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='ingredient_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.ingredienttype'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='tags',
            field=models.ManyToManyField(blank=True, to='menu.tag'),
        ),
    ]