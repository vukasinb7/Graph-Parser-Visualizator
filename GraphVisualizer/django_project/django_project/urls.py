"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import pkg_resources
from django.contrib import admin
from django.urls import path, include

def load_plugins(group_id):
    paths = []
    for ep in pkg_resources.iter_entry_points(group=group_id):
        if str(ep).split('=')[0].strip() == 'path':
            paths.append(str(ep).split('=')[1].strip())
    return paths

URLS = set(load_plugins('urls.load'))

urlpatterns = [
    path('admin/', admin.site.urls)]

for url in URLS:
    urlpatterns.append(path("", include(url)))
