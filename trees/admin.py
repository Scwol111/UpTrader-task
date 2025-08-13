from django.contrib import admin

from trees.models import MenuItem

# Register your models here.

@admin.register(MenuItem)
class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent']
