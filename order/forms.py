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
	
	# def clean_title(self):
	# 	# title = self.cleaned_data['title']
	# 	# if 'Django' not in title:
	# 	# 	raise ValidationError('We only accept notes about Django!')
	# 	# return title
	# 	pass