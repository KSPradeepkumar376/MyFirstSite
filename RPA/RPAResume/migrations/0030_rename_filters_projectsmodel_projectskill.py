# Generated by Django 4.1.7 on 2023-04-14 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RPAResume', '0029_rename_filter_projectsmodel_filters'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectsmodel',
            old_name='Filters',
            new_name='ProjectSkill',
        ),
    ]