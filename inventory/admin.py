from django.contrib import admin

# Register your models here.
# Sample Model for testing
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'in_stock', 'created_at')
