from django.db.models import Count, Q
from django.db import models


class Products(models.Model):
    CATEGORY_CHOICES = [
        ('clothing', 'Clothing'),
        ('household', 'household'),
        ('toys', 'Toys'),
        ('stationary', 'Stationary'),
    ]

    user_id = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products', default='null')
    keywords = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    website = models.URLField(blank=True)
    document_upload = models.FileField(upload_to='documents', blank=True)
    description = models.TextField()
    user_id = models.IntegerField(default=0, null=True)
    keywords = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Example usage:
# Assuming you have an organization object and a queryset of product objects

