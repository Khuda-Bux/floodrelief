from django.contrib import admin
from .models import Relief
# Register your models here.
@admin.register(Relief)
class ReliefAdmin(admin.ModelAdmin):
    list_display=['id','name','nic','district','tehsil','uc','mobile_number',
    'photo','date']
