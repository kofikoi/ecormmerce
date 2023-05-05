from django.contrib import admin
from .models import Order
from accounts.models import User

class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'product', 'quantity', 'date_ordered']
    list_filter = ['date_ordered']
    search_fields = ['name', 'email', 'product__name']

admin.site.register(Order, OrderAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email' ]
    search_fields = ['name']

admin.site.register(User, UserAdmin)

