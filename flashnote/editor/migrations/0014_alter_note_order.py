# Generated by Django 5.0.6 on 2024-05-26 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0013_note_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]
