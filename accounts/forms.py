from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'is_employer']
        labels = {
            'is_employer' : ('Employer Account')
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class ProfileUpdate(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ( 'image', 'description', 'cv',)

        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }