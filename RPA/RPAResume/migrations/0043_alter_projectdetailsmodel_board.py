# Generated by Django 4.1.7 on 2023-04-20 06:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RPAResume', '0042_alter_projectdetailsmodel_board'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetailsmodel',
            name='board',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(default=[], null=True), size=5),
        ),
    ]
