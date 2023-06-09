# Generated by Django 4.1.7 on 2023-04-14 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RPAResume', '0026_personaldetailsmodels_domain'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False)),
                ('Pic', models.URLField(default=None, max_length=254)),
                ('Projectlink', models.URLField(default=None, max_length=254)),
                ('Projects_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RPAResume.personaldetailsmodels')),
            ],
            options={
                'db_table': 'Projects',
            },
        ),
    ]
