# Generated by Django 5.0.6 on 2024-05-18 04:30

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0005_alter_note_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
