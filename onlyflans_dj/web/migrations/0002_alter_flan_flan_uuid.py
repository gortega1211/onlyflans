# Generated by Django 4.2.8 on 2024-04-18 23:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flan',
            name='flan_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]