# Generated by Django 3.0.7 on 2020-06-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('tech', models.CharField(max_length=15)),
                ('describ', models.CharField(max_length=100)),
                ('link', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
    ]
