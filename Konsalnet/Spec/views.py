from django.shortcuts import render
from .forms import RamForm, NewRamForm, NewCityAdd
from .models import SpecRamAdd, CityAdd
from django import forms
# Create your views here.

def Add(request):
    nowa_specyfikacja = NewRamForm()
    nowa_city = NewCityAdd()
    if request.method == "POST":
        nowa_specyfikacja = NewRamForm(request.POST)
        nowa_city = NewCityAdd(request.POST)
        if nowa_specyfikacja.is_valid():
            SpecRamAdd.objects.create(**nowa_specyfikacja.cleaned_data)
            nowa_specyfikacja = NewRamForm()
        elif nowa_city.is_valid():
            CityAdd.objects.create(**nowa_city.cleaned_data)
            nowa_city = NewCityAdd()

    context = {
            'form': nowa_specyfikacja,
            'formCity' : nowa_city
    }
    return render(request, 'Add.html', context)

def AddRam(request):
    return render(request, 'AddRam.html')