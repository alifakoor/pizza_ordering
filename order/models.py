from django.db import models
from django.contrib.auth.models import User
from pizza.models import Pizza


class Order(models.Model):
	SIZE_OPTIONS = (
		("s", "Small"),
		("m", "Medium"),
		("l", "Large")
	)

	STATUS = (
		("r", "received"),
		("p", "preparing"),
		("d", "delivered")
	)

	size = models.CharField(choices=SIZE_OPTIONS, max_length=1)
	quantity = models.PositiveSmallIntegerField()
	status = models.CharField(choices=STATUS, max_length=1)
	created_at = models.DateTimeField(auto_now_add=True)
	delivered_at = models.DateTimeField(null=True, blank=True)
	pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='pizza')
	customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
