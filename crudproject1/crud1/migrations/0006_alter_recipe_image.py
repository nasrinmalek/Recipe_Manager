# Generated by Django 5.0.2 on 2024-04-19 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud1', '0005_alter_recipe_ingredients_alter_recipe_instructions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='recipe_images/'),
        ),
    ]
