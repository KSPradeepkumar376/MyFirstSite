# Generated by Django 4.1.7 on 2023-04-13 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RPAResume', '0022_personaldetailsmodels_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetailsmodels',
            name='Location',
            field=models.URLField(default=None, null=True),
        ),
    ]
