"""djangodrfSample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    # path('', views.profile_list, name='profile_list')
    # path('', views.ProfileView.as_view(), name='profile_list')
    path('<int:pk>', views.ProfileRetrieve.as_view(), name='profile_list')
]

# url for check RetrieveAPIView
#  http: // 127.0.0.1:8000/profiles/1
