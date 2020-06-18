from django.contrib import admin
from django.urls import path

from account.views import Dashboard, LoginView,PersonalInfoView,signout

urlpatterns = [
    path('dashboard/', Dashboard.as_view(),name='dashboard'),
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', signout,name='signout'),
    path('personal_info/', PersonalInfoView.as_view(),name='add_personal_info'),
]