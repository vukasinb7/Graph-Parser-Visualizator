from django.urls import path
from . import views

urlpatterns = [
    path('layout/simple',views.layout_simple, name="layout_simple")
]