# Generated by Django 4.2 on 2023-07-03 13:16

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='icon_image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, help_text='Gallery Icon Image', null=True, upload_to='Gallery/icon-images'),
        ),
    ]
