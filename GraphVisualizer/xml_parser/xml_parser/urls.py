from . import views
from django.urls import path

urlpatterns = [
    path('parser/xml/<str:name>', views.parser_xml, name="parser_xml")
]
