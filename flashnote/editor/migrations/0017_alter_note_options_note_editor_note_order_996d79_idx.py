# Generated by Django 5.0.6 on 2024-05-27 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0016_alter_note_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['order']},
        ),
        migrations.AddIndex(
            model_name='note',
            index=models.Index(fields=['order'], name='editor_note_order_996d79_idx'),
        ),
    ]