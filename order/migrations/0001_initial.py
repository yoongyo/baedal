# Generated by Django 2.1 on 2020-04-18 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0005_auto_20200418_1457'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum_price', models.CharField(max_length=50)),
                ('menus', models.TextField()),
                ('dateTime', models.DateTimeField(auto_now_add=True, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('pay_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.PayMethod')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
