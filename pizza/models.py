from django.db import models


class Pizza(models.Model):
	name = models.CharField(max_length=50)
	image = models.FileField(upload_to='static/pizza')
	created_at = models.DateTimeField(auto_now_add=True)
