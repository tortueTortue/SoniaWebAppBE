from django.contrib import admin

# Register your models here.

from .models import ModuleName,Layout,Module

admin.site.register(ModuleName)
admin.site.register(Layout)
admin.site.register(Module)
