# Generated by Django 5.0.6 on 2024-05-17 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0002_note_created_note_updated_question_created_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]