# Generated by Django 2.1 on 2020-04-18 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
