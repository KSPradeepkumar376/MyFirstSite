# Generated by Django 4.1.7 on 2023-04-13 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RPAResume', '0019_alter_socialmodel_facebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmodel',
            name='Facebook',
            field=models.URLField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='socialmodel',
            name='instagram',
            field=models.URLField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='socialmodel',
            name='linkedin',
            field=models.URLField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='socialmodel',
            name='skype',
            field=models.URLField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='socialmodel',
            name='twitter',
            field=models.URLField(default=None, max_length=254),
        ),
    ]