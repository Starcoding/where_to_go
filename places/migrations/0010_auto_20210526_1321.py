# Generated by Django 3.2.3 on 2021-05-26 10:21

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_auto_20210526_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
