from django import forms
from .models import Address
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border bg-gray-100'
INPUT_CLASSES_REQUIRED = 'w-full py-4 px-6 rounded-xl border bg-green-100'
class NewAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('first_name', 'middle_name','last_name','voivodeship','nationality','city','street','house_number','zip_code','E_mail','Phone_number')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class':INPUT_CLASSES_REQUIRED
            }),
            'middle_name': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'last_name': forms.TextInput(attrs={
                'class':INPUT_CLASSES_REQUIRED
            }),
            'voivodeship': forms.Select(attrs={
                'class':INPUT_CLASSES_REQUIRED
            }),
            'nationality': forms.TextInput(attrs={
                'class':INPUT_CLASSES_REQUIRED
            }),
            'city': forms.TextInput(attrs={
                'class':INPUT_CLASSES_REQUIRED
            }),
            'street': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'house_number': forms.NumberInput(attrs={
                'class':INPUT_CLASSES_REQUIRED
            }),
            'zip_code': forms.TextInput(attrs={
                'class':INPUT_CLASSES_REQUIRED
            }),
            'E_mail': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'Phone_number': forms.NumberInput(attrs={
                'class':INPUT_CLASSES_REQUIRED
            }),
        }
class EditAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('first_name', 'middle_name','last_name','voivodeship','nationality','city','street','house_number','zip_code','E_mail','Phone_number')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class':INPUT_CLASSES_REQUIRED
            }),
            'middle_name': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'last_name': forms.TextInput(attrs={
                'class':INPUT_CLASSES_REQUIRED
            }),
            'voivodeship': forms.Select(attrs={
                'class':INPUT_CLASSES_REQUIRED
            }),
            'nationality': forms.TextInput(attrs={
                'class':INPUT_CLASSES_REQUIRED
            }),
            'city': forms.TextInput(attrs={
                'class':INPUT_CLASSES_REQUIRED
            }),
            'street': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'house_number': forms.NumberInput(attrs={
                'class':INPUT_CLASSES_REQUIRED
            }),
            'zip_code': forms.TextInput(attrs={
                'class':INPUT_CLASSES_REQUIRED
            }),
            'E_mail': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'Phone_number': forms.NumberInput(attrs={
                'class':INPUT_CLASSES_REQUIRED
            }),
        }