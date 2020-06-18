from django import forms
from .models import Skill, Education,Experience


class SkillForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Skills in rating of 1-5'}))

    class Meta:
        model = Skill
        fields = '__all__'


class EducationForm(forms.ModelForm):
    degree = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Degree'}))
    program = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Program'}))
    board = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Board'}))
    institution = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Institution Name'}))
    graduation_year = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','type':'date','placeholder': 'Graduation Year'}))

    class Meta:
        model = Education
        fields = '__all__'


class ExperienceForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}))
    organization = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Organization Name'}))
    job_location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Job Location'}))
    level = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Job Level'}))
    responsibility = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Responsibilities'}))
    work_hour = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Work Hour'}))
    start_date = forms.CharField(widget=forms.DateInput(attrs={'class': 'form-control','type':'date','placeholder': 'Job start Date'}))
    end_date = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','type':'date','placeholder': 'Job end date'}))

    class Meta:
        model = Experience
        fields = '__all__'
