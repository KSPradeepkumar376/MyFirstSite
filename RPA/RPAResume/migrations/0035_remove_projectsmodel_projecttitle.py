# Generated by Django 4.1.7 on 2023-04-17 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RPAResume', '0034_alter_projectsmodel_projecttitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectsmodel',
            name='ProjectTitle',
        ),
    ]
