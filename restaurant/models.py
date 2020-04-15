from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Area(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RestaurantCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    admin = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(RestaurantCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo')
    address = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    introduction = models.TextField()

    closedDay = models.CharField(max_length=50)
    businessHours = models.CharField(max_length=50)

    businessLicenseRepresentative = models.CharField(max_length=50)
    businessLicenseMutualName = models.CharField(max_length=50)
    businessLicenseNumber = models.CharField(max_length=50)

    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='follow', blank=True)

    representative_menu = models.CharField(max_length=50)
    delivery_requirement_time = models.CharField(max_length=50)

    minimum_order_price = models.CharField(max_length=50)

    deliverable_area = models.ManyToManyField(Area, related_name='deliverable_area', blank=True)

    def __str__(self):
        return self.name


class MenuCategory(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    popular = models.BooleanField(default=False)
    soldOut = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    content = models.TextField()
    image1 = models.ImageField(upload_to='review_image/', blank=True, null=True)
    image2 = models.ImageField(upload_to='review_image/', blank=True, null=True)
    image3 = models.ImageField(upload_to='review_image/', blank=True, null=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.restaurant.name





