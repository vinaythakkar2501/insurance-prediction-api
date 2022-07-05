"""mlbackend URL Configuration

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
# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from mlpredict import views as v
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'medical-insurance',v.FeaturesView,'prediction')
# router.register(r'life-insurance',v.FeaturesView,'prediction')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.index),
    path('medical-predict/',v.medicalform),
    # path('api/',include(router.urls)),
    path('api/medical-insurance/',v.MedicalDataList.as_view()),
    path('api/life-insurance/',v.LifeDataList.as_view()),
    path('api/car-price/',v.CarDataList.as_view())
]
