from django import forms
from phonenumber_field.formfields import PhoneNumberField
from dashboard import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Row, Submit, Button, Column


class HomeForm(forms.ModelForm): 
    
    name =  forms.CharField(
        required = True,
        label='Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name',
            }
        )
    )
    
    house_no =  forms.CharField(
        required = True,
        label='House Number',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'House No.',
            }
        )
    )

    owner_name =  forms.CharField(
        required = True,
        label='Owner\'s Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Owner\'s Name',
            }
        )
    )
    
    owner_email =  forms.CharField(
        required = True,
        label='Owner\'s Email',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Owner\'s Email',
                'type': 'email'
            }
        )
    )
    phone_number = PhoneNumberField(
        required = True,
        label='Phone No.',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Phone No.',
                'required': True
            }
        ),
    )
    def __init__(self, *args, **kwargs):
        super(HomeForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control form-control-alternative',
            }) 

    class Meta:
        model = models.Home
        fields = ['name', 'house_no', 'owner_name', 'owner_email', 'phone_number']