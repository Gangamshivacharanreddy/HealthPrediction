# predict/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_heart_disease, name='predict_view'),
]