from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
class showAssignmetsAdmin(admin.ModelAdmin):
    list_display=('name','file','date')
    
admin.site.register(sbmtAssignment,showAssignmetsAdmin)

class showComplain(admin.ModelAdmin):
    list_display=('email','complain')
    
admin.site.register(complaint,showComplain)

admin.site.register(thoughts)


class chatAdmin(admin.ModelAdmin):
    list_display=('query','responce')
admin.site.register(chat,chatAdmin)

admin.site.register(chatBase)