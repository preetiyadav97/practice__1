from django.contrib import admin
from .models import detail

# Register your models here.

class detailAdmin(admin.ModelAdmin):
    model=detail
    list_display=['firstname','seondname','email','salary']
    

admin.site.register(detail, detailAdmin)
