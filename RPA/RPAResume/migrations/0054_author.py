# Generated by Django 4.1.7 on 2023-04-22 06:23

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RPAResume', '0053_delete_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=512)),
                ('books', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=512), size=None)),
                ('Author_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RPAResume.projectsmodel')),
            ],
            options={
                'db_table': 'Author',
            },
        ),
    ]