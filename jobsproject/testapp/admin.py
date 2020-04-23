from django.contrib import admin
from testapp.models import Hydjobs,Bengalorejobs,Delhijobs,punejobs

# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display = ['name','eligibility','address','email','phonenumber']
admin.site.register(Hydjobs,HydjobsAdmin)

class BangalorejobsAdmin(admin.ModelAdmin):
    list_display = ['name', 'eligibility','address','email','phonenumber']
admin.site.register(Bengalorejobs,BangalorejobsAdmin)

class DelhijobsAdmin(admin.ModelAdmin):
    list_display = ['name','address','eligibility', 'email','phonenumber']
admin.site.register(Delhijobs,DelhijobsAdmin)

class punejobsAdmin(admin.ModelAdmin):
    list_display = ['name','address','eligibility',  'email','phonenumber']
admin.site.register(punejobs,punejobsAdmin)
