from . import views
from django.urls import path

urlpatterns = [
    path('parser/json/<str:name>', views.parser_json, name="parser_json")
]
