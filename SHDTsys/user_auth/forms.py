# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
# , UserDetail


# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(label="", widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
#     first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'First Name'}))
#     last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name',
#                   'email', 'password1', 'password2')

#     def __init__(self, *args, **kwargs):
#         super(SignUpForm, self).__init__(*args, **kwargs)

#         self.fields['username'].widget.attrs['class'] = 'form-control'
#         self.fields['username'].widget.attrs['placeholder'] = 'User Name'
#         self.fields['username'].label = ''
#         self.fields['username'].help_text = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'

#         self.fields['password1'].widget.attrs['class'] = 'form-control'
#         self.fields['password1'].widget.attrs['placeholder'] = 'Password'
#         self.fields['password1'].label = ''
#         self.fields['password1'].help_text = 'Your password must contain at least 8 characters and should not be entirely numeric.'

#         self.fields['password2'].widget.attrs['class'] = 'form-control'
#         self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
#         self.fields['password2'].label = ''
#         self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


 
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    class Meta:
        model = User
        fields = ('email','name','role')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

# class UserDetailsForm(forms.ModelForm):
#     date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
#     name = forms.CharField(max_length=100)
    
#     class Meta:
#         model = UserDetail
#         fields = ('phone_number', 'date_of_birth', 'city', 'state','profile_picture')
#         labels={'profile_picture':""}