# Generated by Django 3.2.8 on 2021-11-26 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galaa', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photos',
            old_name='image_name',
            new_name='name',
        ),
    ]
