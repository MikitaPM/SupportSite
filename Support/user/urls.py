from django.urls import path
from .views import RegistrUserView


urlpatterns= [
    path('registr/', RegistrUserView.as_view(), name='registr')
]