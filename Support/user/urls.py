from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns= [
    path('api/v1/', include(api_urlpatterns)),
]