# Generated by Django 5.0.6 on 2024-06-16 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Availability',
            field=models.BooleanField(default=True),
        ),
    ]
