# Generated by Django 4.2.20 on 2025-04-09 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShortsKeys',
            new_name='ShortKeys',
        ),
        migrations.RenameField(
            model_name='shortkeys',
            old_name='key_nmae',
            new_name='key_name',
        ),
    ]
