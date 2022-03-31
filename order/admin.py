from django.contrib import admin
from datetime import datetime

from . import models


@admin.action(description='Change Selected Orders as Preparing')
def make_preparing(modeladmin, request, queryset):
	queryset.update(status="p")

@admin.action(description='Change Selected Orders as Received')
def make_delivered(modeladmin, request, queryset):
	queryset.update(status="d", delivered_at=datetime.now())

class OrdersAdmin(admin.ModelAdmin):
	list_display = ('size', 'quantity', 'status', 'created_at', 'delivered_at', 'customer')
	ordering = ['created_at']
	actions = [make_preparing, make_delivered]

admin.site.register(models.Order, OrdersAdmin)
