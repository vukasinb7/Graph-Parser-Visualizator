from django.contrib import admin

from .models import *

admin.site.register(Graph)
admin.site.register(Node)
admin.site.register(Edge)
admin.site.register(KeyVal)

# Register your models here.
