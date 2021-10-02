from django import forms
from .models import Image
class Myimage(forms.ModelForm):
	class Meta:	
		model=Image
		fields='__all__'
		labels = {'image':''}
