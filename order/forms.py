from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, NumberInput, Select

from .models import Order

class OrdersForm(ModelForm):
	class Meta:
		model = Order
		fields = ('title','size', 'quantity')
		widgets = {
			'title': TextInput(attrs={'class': 'form-control'}),
			'size': Select(attrs={'class': 'form-select'}),
			'quantity': NumberInput(attrs={'class': 'form-control'})
		}
	
	def clean_quantity(self):
		size = self.cleaned_data['size']
		if size not in Order.SIZE_OPTIONS:
			raise ValidationError('We only have 3 sizes!')
		return size

	def clean_quantity(self):
		quantity = self.cleaned_data['quantity']
		if quantity <= 0:
			raise ValidationError('You must order at least 1 quantity.')
		return quantity
