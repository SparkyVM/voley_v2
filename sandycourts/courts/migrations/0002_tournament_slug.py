# Generated by Django 5.1 on 2024-08-07 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
    ]
