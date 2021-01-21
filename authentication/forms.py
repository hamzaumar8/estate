from django import forms
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm 
from phonenumber_field.formfields import PhoneNumberField

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control form-control-alternative',
            }) 

    department = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your Department / Agency',
            'required': True
        }),
    )


    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        cleaned_data = super(CustomSignupForm, self).clean()
        user_profile = user.profile
        user_profile.department = cleaned_data['department']
        user.save() 
        user_profile.save()
        return user

