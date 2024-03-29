from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from accounts.models import User


class RegisterForm(forms.Form):
    phone = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'شماره تلفن'}) , validators=[validators.MaxLengthValidator(11)])
    username = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'نام کاربری'}))
    Full_name = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'نام'}))
    email = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'ایمیل'}))

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if len(phone)<11:
            raise ValidationError("This Information is not correct")
        return phone

class Edit_Profile_Form(forms.ModelForm):
    phone = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'شماره تلفن'}) , validators=[validators.MaxLengthValidator(11)] , required=False)
    class Meta:
        model=User
        fields=['Full_name', 'username' , 'email' , 'phone']
        widgets={
            'username':forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'نام کاربری'}),
            'Full_name' :forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'نام و نام خانوادگی'}),
            'email' :forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'ایمیل'}),
        }