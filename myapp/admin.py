from django.contrib import admin
from .models import myModel

class myModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(myModel,myModelAdmin)

