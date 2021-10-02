from django.contrib import admin
from .models import Image
# Register your models here.

class Myimage(admin.ModelAdmin):
	list_display=['id','image','date']

admin.site.register(Image,Myimage)	