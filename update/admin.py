from django.contrib import admin
from .models import addof

# Register your models here.

class addofAdmin(admin.ModelAdmin):
    list_display = ('id','name',)


admin.site.register(addof, addofAdmin)

