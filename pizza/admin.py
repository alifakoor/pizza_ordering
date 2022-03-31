from django.contrib import admin

from . import models


class PizzaAdmin(admin.ModelAdmin):
	list_display = ('name', 'created_at')
	ordering = ['created_at']

admin.site.register(models.Pizza, PizzaAdmin)
