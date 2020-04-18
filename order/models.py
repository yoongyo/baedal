from django.db import models
from django.conf import settings

import sys
sys.path.append('..')
from restaurant.models import Review, Restaurant, PayMethod


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    sum_price = models.CharField(max_length=50)
    menus = models.TextField()
    pay_method = models.ForeignKey(PayMethod, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.menus