# Generated by Django 4.2 on 2023-07-03 13:07

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='icon_image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, help_text='Carousel Icon image', null=True, upload_to='Carousel/icon_images'),
        ),
    ]