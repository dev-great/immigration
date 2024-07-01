from django.urls import path
from .views import I90ApplicationCreateView

urlpatterns = [
    path('i90-form/', I90ApplicationCreateView.as_view(), name='i90-form'),
]
