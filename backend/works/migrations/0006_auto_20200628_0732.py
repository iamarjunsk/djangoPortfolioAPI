# Generated by Django 3.0.7 on 2020-06-28 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0005_works_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='image',
            field=models.ImageField(default="pics/'helo", max_length='50', upload_to='pics'),
        ),
    ]
