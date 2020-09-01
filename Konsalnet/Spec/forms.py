from django.forms import ModelForm
from django import forms

from .models import SpecRamAdd, Options


class RamForm(ModelForm):
    class Meta:
        model = SpecRamAdd
        fields = ('Computer','Ram',)

class NewRamForm(forms.Form):
    Computer = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id':'buttonToolbar'}), label='')
    Ram = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id':'buttonToolbar'}),label='')

class NewCityAdd(forms.Form):
    City = forms.CharField(required = False, max_length=100,widget=forms.TextInput(attrs={'id':'buttonToolbar'}),label='')
    Meters = forms.IntegerField(required = False, widget=forms.TextInput(attrs={'id':'buttonToolbar'}),label='')

class ChoiceFieldOrder(forms.Form):
    ChoiceFieldComputer = forms.ModelChoiceField(queryset=SpecRamAdd.objects, empty_label="Wybierz model")

class OptionValue(ModelForm):
    pass
    class Meta:
        model = Options
        fields = ('NameHost','NameMail','PassMail','NameToSend','NamePort',)

class OptionsField(forms.Form):
    NameHost = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'id':'buttonToolbar'}), label='')
    NameMail = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'id':'buttonToolbar'}),label='')
    PassMail = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'id':'buttonToolbar'}),label='')
    NameToSend = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'id':'buttonToolbar'}),label='')
    NamePort = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'id':'buttonToolbar'}),label='')