# Generated by Django 2.1 on 2020-04-18 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20200418_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='follow',
        ),
    ]
