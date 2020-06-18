from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from contact.forms import ContactForm
from contact.models import Contact


class ContactView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'backend/contact.html'

    def get(self, request):
        context = {
            'contacts': Contact.objects.all()
        }
        return render(request, self.template_name, context)


def contactStatusUpdate(request, id):
    Contact.objects.filter(pk=id).update(status=True)
    return redirect('contact')
