from django.urls import path
from . import views

urlpatterns = [
  path("", views.HomePage ),
  path("simple", views.simple),
  path("tipper", views.inputs),
  path("results", views.calculateTip)
]
