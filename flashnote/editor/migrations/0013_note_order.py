# Generated by Django 5.0.6 on 2024-05-26 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0012_remove_page_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
