from django import forms
from cars.models import Car


class AddForm(forms.ModelForm):
	class Meta:
		model = Car
		exclude = [""]