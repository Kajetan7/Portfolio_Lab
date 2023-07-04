from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=64)


class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    TYPES = [
        (1, 'Fundacja'),
        (2, 'Organizacja pozarzadowa'),
        (3, 'Zbiorka lokalna'),
    ]
    type = models.CharField(max_length=32, choices=TYPES, default=1)
    categories = models.ManyToManyField(Category, null=True, through='InstitutionCategory')


class InstitutionCategory(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category, null=True, through='DonationCategory')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=16)
    city = models.CharField(max_length=16)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, default=None)


class DonationCategory(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
