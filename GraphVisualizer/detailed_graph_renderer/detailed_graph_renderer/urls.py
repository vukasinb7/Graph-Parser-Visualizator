from django.urls import path
from . import views

urlpatterns = [
    path('layout/detailed',views.layout_detailed, name="layout_detailed")
]