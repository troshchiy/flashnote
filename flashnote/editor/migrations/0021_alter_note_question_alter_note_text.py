# Generated by Django 5.0.6 on 2024-05-29 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0020_alter_note_last_review_alter_note_next_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='question',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]