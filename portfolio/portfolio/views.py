from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from account.models import PersonalInfo
from contact.models import Contact
from info.models import Skill, Education, Experience


class FrontView(View):
    template_name = 'frontend/master/front.html'

    def get(self, request):
        print(Experience.objects.all())
        context = {
            'skills': Skill.objects.all(),
            'personal': PersonalInfo.objects.filter(pk='1').get(),
            'educations': Education.objects.all(),
            'experiences': Experience.objects.all(),
        }
        return render(request, self.template_name,context)

    def post(self, request, *args, **kwargs):
        n = request.POST.get('name')
        e = request.POST.get('email')
        p = request.POST.get('phone_number')
        m = request.POST.get('message')

        Contact.objects.create(name=n, email=e, phone_number=p, message=m)
        messages.add_message(request, messages.SUCCESS, "Message Successfully Sent")
        return redirect('master')