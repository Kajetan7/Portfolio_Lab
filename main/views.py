from django.shortcuts import render
from django.views import View
from django.db.models import Sum
from main.models import *


class LandingPage(View):
    def get(self, request):
        context = {
            'quantity_of_donations': Donation.objects.aggregate(total=Sum('quantity'))['total'],
            'quantity_of_institutions': Institution.objects.count(),
            'foundations': Institution.objects.filter(type=1),
            'non_government_organizations': Institution.objects.filter(type=2),
            'local_charities': Institution.objects.filter(type=3)
        }
        return render(request, 'index.html', context)


class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')
