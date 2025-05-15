from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_brain_stroke, name='brain_stroke_predict'),
]