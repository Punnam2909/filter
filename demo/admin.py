from django.contrib import admin
from .models import Surname,Member

# Register your models here.

class SurnameAdmin(admin.ModelAdmin):
    list_display = ('id','family_name',)
    list_filter = ('family_name',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
admin.site.register(Surname, SurnameAdmin)


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id','person_name',)
    list_filter = ('person_name',)


admin.site.register(Member, MemberAdmin)

