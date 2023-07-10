from django.contrib import admin
from django import forms
from main.models import *


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = '__all__'


class InstitutionAdmin(admin.ModelAdmin):
    form = InstitutionForm


admin.site.register(Institution, InstitutionAdmin)
