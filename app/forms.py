from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField,PasswordChangeForm,PasswordResetForm, SetPasswordForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from django.utils.translation import gettext,gettext_lazy as _
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),label_suffix=' ')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32, help_text='First name',label_suffix=' ')
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32, help_text='Last name',label_suffix=' ',required=False)
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email',}), max_length=64, help_text='Enter a valid email address',label_suffix=' ',required=True)
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),label_suffix=' ',help_text="helo")
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),label_suffix=' ',help_text="helo")
    
    class Meta(UserCreationForm.Meta):
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
        labels={'email':'Email'}
        label_suffix={'username':' '}

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_("Password"), strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'})) 

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True,'class':'form-control'}),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
    )
class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email','autofocus': True,'class':'form-control'})
    )

class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','autofocus': True,'class':'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
    )


class UserProfileForm(forms.ModelForm):
        
    class Meta:
        model = UserProfile
        fields = ("name","locality","landmark","city","zipcode","state")
        widgets= {"name":forms.TextInput(attrs={'autofocus': True,'class':'form-control'}),
                    "landmark":forms.TextInput(attrs={'class':'form-control'}),
                    "locality":forms.TextInput(attrs={'class':'form-control'}),
                    "city":forms.TextInput(attrs={'class':'form-control'}),
                    "zipcode":forms.NumberInput(attrs={'class':'form-control'}),
                    "state":forms.Select(attrs={'class':'form-control'}),
                    }
    