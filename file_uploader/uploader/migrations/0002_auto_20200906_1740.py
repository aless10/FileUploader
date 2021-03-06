# Generated by Django 3.1.1 on 2020-09-06 17:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='password',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='slug',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
