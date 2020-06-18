from django import forms
from .models import PersonalInfo


class PersonalInfoForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','type':'email', 'placeholder': 'Email'}))
    mobile = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}))
    gender = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gender'}))
    nationality = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nationality'}))
    religion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Religion'}))
    date_of_birth = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','type':'date', 'placeholder': 'Date of Birth'}))
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control','type':'file'}))

    class Meta:
        model = PersonalInfo
        fields = '__all__'