# Generated by Django 4.1.7 on 2023-03-14 04:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('RPAResume', '0004_alter_personaldetailsmodels_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetailsmodels',
            name='id',
            field=models.AutoField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
    ]
