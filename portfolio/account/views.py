from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
# Create your views here.
from django.views import View

from account.forms import PersonalInfoForm
from account.models import PersonalInfo


class LoginView(View):
    template_name = 'backend/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        e = request.POST.get('email')
        p = request.POST.get('password')
        user = authenticate(email=e, password=p)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, "login Credential does not match")
            return redirect('login')

def signout(request):
    logout(request)
    return redirect('login')

class Dashboard(View):
    template_name = 'backend/dashboard.html'

    def get(self, request):
        return render(request, self.template_name)


class PersonalInfoView(View):
    template_name = 'backend/add_personal_info.html'

    def get(self, request):
        context = {
            'form': PersonalInfoForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Personal info Added")
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, "Personal Info Addition Failed")
            return redirect('add_personal_info')
    # def post(self, request, *args, **kwargs):
    #     e = request.POST.get('email')
    #     m = request.POST.get('mobile')
    #     a = request.POST.get('address')
    #     g = request.POST.get('gender')
    #     n = request.POST.get('nationality')
    #     r = request.POST.get('religion')
    #     d = request.POST.get('date_of_birth')
    #     p = request.POST.get('photo')
    #
    #     PersonalInfo.objects.create(email=e, mobile=m, address=a, nationality=n,gender=g,religion=r,photo=p,date_of_birth=d)
    #     messages.add_message(request, messages.SUCCESS, "Personal Info Successfully Added")
    #     return redirect('dashboard')