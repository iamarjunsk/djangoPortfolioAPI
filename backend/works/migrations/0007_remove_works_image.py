# Generated by Django 3.0.7 on 2020-06-28 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0006_auto_20200628_0732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='works',
            name='image',
        ),
    ]
