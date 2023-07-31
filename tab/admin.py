from django.contrib import admin
from .models import Place

# Register your models here.
#1 
# admin.site.register(Place)

# 2 Show data in table form with heading

class PlaceAdmin(admin.ModelAdmin):
    model=Place
    list_display=['pl_name','pl_email','pl_phone','pl_image']
    

admin.site.register(Place,PlaceAdmin)

