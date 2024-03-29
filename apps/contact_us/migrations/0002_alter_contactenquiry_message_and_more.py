# Generated by Django 4.2 on 2023-06-30 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactenquiry',
            name='message',
            field=models.TextField(blank=True, help_text='The Enquiry Message', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='contactenquiry',
            name='service',
            field=models.ForeignKey(help_text='The service enquiring about', on_delete=django.db.models.deletion.CASCADE, to='service.service'),
        ),
    ]
