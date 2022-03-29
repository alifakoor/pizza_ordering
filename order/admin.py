from django.contrib import admin
from . import models

class OrdersAdmin(admin.ModelAdmin):
	list_display = ('title', 'size', 'quantity', 'status', 'created_at', 'delivered_at', 'customer')

admin.site.register(models.Order, OrdersAdmin)
