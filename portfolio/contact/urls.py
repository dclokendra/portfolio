from django.contrib import admin
from django.urls import path

from contact.views import ContactView,contactStatusUpdate

urlpatterns = [
    path('list/', ContactView.as_view(),name='contact'),
    path('update_status/<int:id>', contactStatusUpdate,name='update_status'),
]