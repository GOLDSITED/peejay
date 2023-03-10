from django import forms
from django.forms import ModelForm, Textarea
from . models import Item
from .models import Contact


class CheckoutForm(forms.Form):
	street_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
			'placeholder':'1234 main str',
			'class': 'form-control'
		}))
	apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
			'placeholder':'Apartment or Suite',
			'class': 'form-control'
		}))
	phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={
			'placeholder':'Phone Number',
			'class': 'form-control'
		}))
	set_default_shipping = forms.BooleanField(required=False)
	use_default_shipping = forms.BooleanField(required=False)


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title','price','discount_price', 'slug','description','image','category','is_featured', 'num_available','thumbnail']
        widgets = {
            
            'title': forms.TextInput(attrs={'class': 'form-control'}),
			'price': forms.TextInput(attrs={'class': 'form-control'}),
			'discount_price': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
			'num_available': forms.TextInput(attrs={'class': 'form-control'}),
			'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
            

		}

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
	

