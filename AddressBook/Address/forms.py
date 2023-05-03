from django import forms
from .models import Address
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
class NewAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('first_name', 'middle_name','last_name','voivodeship','nationality','city','street','house_number','zip_code','E_mail','Phone_number')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'middle_name': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'last_name': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'voivodeship': forms.Select(attrs={
                'class':INPUT_CLASSES
            }),
            'nationality': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'city': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'street': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'house_number': forms.NumberInput(attrs={
                'class':INPUT_CLASSES
            }),
            'zip_code': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'E_mail': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'Phone_number': forms.NumberInput(attrs={
                'class':INPUT_CLASSES
            }),
        }
class EditAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('first_name', 'middle_name','last_name','voivodeship','nationality','city','street','house_number','zip_code','E_mail','Phone_number')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'middle_name': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'last_name': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'voivodeship': forms.Select(attrs={
                'class':INPUT_CLASSES
            }),
            'nationality': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'city': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'street': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'house_number': forms.NumberInput(attrs={
                'class':INPUT_CLASSES
            }),
            'zip_code': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'E_mail': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'Phone_number': forms.NumberInput(attrs={
                'class':INPUT_CLASSES
            }),
        }