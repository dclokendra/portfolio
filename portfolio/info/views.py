from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from .forms import SkillForm, EducationForm, ExperienceForm
from .models import Skill, Education, Experience


class SkillAddView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'backend/add_skill.html'

    def get(self, request):
        context = {
            'form': SkillForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = SkillForm(request.POST, request.FILES or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.add_message(request, messages.SUCCESS, "Skill added Successfully")
            return redirect('skill')
        else:
            messages.add_message(request, messages.ERROR, "Skill creation Failed")
            return redirect('add_skill')


class SkillView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'backend/skill.html'

    def get(self, request):
        context = {
            'skills': Skill.objects.all()
        }
        return render(request, self.template_name, context)


def skillEditView(request, id):
    form = SkillForm(request.POST or None, instance=Skill.objects.get(pk=id))
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Successfully updated")
        return redirect('skill')
    return render(request, 'backend/edit_skill.html', {'form': form})


def deleteSkill(request, id):
    a = Skill.objects.get(pk=id)
    a.delete()
    messages.add_message(request, messages.SUCCESS, "Successfully deleted")
    return redirect('skill')


# education
class EducationAddView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'backend/add_education.html'

    def get(self, request):
        context = {
            'form': EducationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Education Created Successfully")
            return redirect('education')
        else:
            messages.add_message(request, messages.ERROR, "Education creation Failed")
            return redirect('add_education')


class EducationView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'backend/education.html'

    def get(self, request):
        context = {
            'educations': Education.objects.all()
        }
        return render(request, self.template_name, context)


def educationEditView(request, id):
    form = EducationForm(request.POST or None, instance=Education.objects.get(pk=id))
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Successfully updated")
        return redirect('education')
    return render(request, 'backend/edit_education.html', {'form': form})


def deleteEducation(request, id):
    a = Education.objects.get(pk=id)
    a.delete()
    messages.add_message(request, messages.SUCCESS, "Successfully deleted")
    return redirect('education')


# experience
class ExperienceAddView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'backend/add_experience.html'

    def get(self, request):
        context = {
            'form': ExperienceForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Experience Created Successfully")
            return redirect('experience')
        else:
            messages.add_message(request, messages.ERROR, "Experience creation Failed")
            return redirect('add_experience')


class ExperienceView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'backend/experience.html'

    def get(self, request):
        context = {
            'experiences': Experience.objects.all()
        }
        return render(request, self.template_name, context)


def experienceEditView(request, id):
    form = ExperienceForm(request.POST or None, instance=Experience.objects.get(pk=id))
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Successfully updated")
        return redirect('experience')
    return render(request, 'backend/edit_experience.html', {'form': form})


def deleteExperience(request, id):
    a = Experience.objects.get(pk=id)
    a.delete()
    messages.add_message(request, messages.SUCCESS, "Successfully deleted")
    return redirect('experience')
