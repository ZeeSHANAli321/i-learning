from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
admin.site.register(eNotes)

class batchadmin(admin.ModelAdmin):
    list_display = ('name','price','about','instructor_name','finalPrice','discount','display_icon')
    def display_icon(self,obj):
        return format_html('<img src="{}" width="auto" height="150" />', obj.icon.url)
    display_icon.short_description = 'icon'

    def instructor_name(self,obj):
        return obj.instructor.name if obj.instructor else None
    

    instructor_name.short_description = 'instructor'
admin.site.register(batch,batchadmin)


#signUp model admin 
class signUpModelAdmin(admin.ModelAdmin):
    list_display = ('fname','lname','email','phone','pswrd','display_batch','display_image')
    def display_image(self, obj):
        return format_html('<img src="{}" width="auto" height="150" />', obj.image.url)

    display_image.short_description = 'Image'

    def display_batch(self, obj):
        # obj is the current Student instance
        return ", ".join([batch.name for batch in obj.sBatch.all()])
    display_batch.short_description = 'sBatch'
admin.site.register(signUpModel,signUpModelAdmin)


#Contact model admin 
class contactModelAdmin(admin.ModelAdmin):
    list_display = ('fname','lname','email','sub','msg','created_at')
admin.site.register(contact,contactModelAdmin)

#video admin 
class videoAdmin(admin.ModelAdmin):
    list_display = ('vTitle','vUrl','vDuration','vDate')
admin.site.register(video,videoAdmin)

#notifications admin 
class notificationAdmin(admin.ModelAdmin):
    list_display = ('nTitle','notification','nDate')
admin.site.register(bnotifications,notificationAdmin)

#instructor admin panel
class instructorAdmin(admin.ModelAdmin):
    list_display=('name','about','qualifications','technologies','channel','showImage')
    def showImage(self,obj):
        return format_html('<img src="{}" width="auto" height="150" />', obj.image.url)
    showImage.short_description='image'
admin.site.register(instructor,instructorAdmin)

#assignments 
class assignmentsAdmin(admin.ModelAdmin):
    list_display=('name','file_url','submitDate')
    def file_url(self,obj):
        return format_html('<p>{}</p>',obj.file.url)
admin.site.register(assignments,assignmentsAdmin)
#student material admin panel
class sMaterialadmin(admin.ModelAdmin):
    list_display =('name','about','fileUrl','display_image')
    def display_image(self, obj):
        return format_html('<img src="{}" width="auto" height="150" />', obj.image.url)
    display_image.short_description = 'Image'
    def fileUrl(self, obj):
        return format_html('<small>{}</small>', obj.file.url)
    fileUrl.short_description = 'File'
admin.site.register(sMaterial,sMaterialadmin)


