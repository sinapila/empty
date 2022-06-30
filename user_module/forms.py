from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from account_module.models import User

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'addres','about_us']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام خانوادگی'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'آواتار'
            }),
            'addres': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'آدرس',
                'rows': '5',
            }),
            'about_us': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'آدرس',
                'rows': '5',
            }),

        }



class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label='کلمه عبور فعلی',
        widget=forms.PasswordInput(
            # attrs={
            #     'class':'form-control'
            # }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(
            # attrs={
            #     'class':'form-control'
            # }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(
            # attrs={
            #     'class':'form-control'
            # }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')






