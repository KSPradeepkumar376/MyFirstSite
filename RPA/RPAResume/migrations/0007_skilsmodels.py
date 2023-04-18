# Generated by Django 4.1.7 on 2023-03-19 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RPAResume', '0006_alter_personaldetailsmodels_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='skilsmodels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Skil1', models.CharField(default=None, max_length=254)),
                ('Skil1Perc', models.IntegerField(default=None, max_length=254)),
                ('Skil2', models.CharField(default=None, max_length=254)),
                ('Skil2Perc', models.IntegerField(default=None, max_length=254)),
                ('Skil3', models.CharField(default=None, max_length=254)),
                ('Skil3Perc', models.IntegerField(default=None, max_length=254)),
                ('Skil4', models.CharField(default=None, max_length=254)),
                ('Skil4Perc', models.IntegerField(default=None, max_length=254)),
                ('Skil5', models.CharField(default=None, max_length=254)),
                ('Skil5Perc', models.IntegerField(default=None, max_length=254)),
                ('Skil6', models.CharField(default=None, max_length=254)),
                ('Skil6Perc', models.IntegerField(default=None, max_length=254)),
                ('Skil_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RPAResume.personaldetailsmodels')),
            ],
        ),
    ]
