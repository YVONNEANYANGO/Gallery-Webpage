from django.contrib import admin
from .models import Photographer,Image,tags

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Photographer)
admin.site.register(Image,ImageAdmin)
admin.site.register(tags)