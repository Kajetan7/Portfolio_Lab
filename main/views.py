from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Sum
from main.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


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

    def post(self, request):
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return redirect('register')
        login(request, user)
        return redirect('landing_page')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('landing_page')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            return render(request, 'register.html', {'message': 'Hasla musza byc jednakowe!'})
        User.objects.create_user(username=email, email=email, password=password, first_name=name, last_name=surname)
        return redirect('login')


