from .models import Application, Job, Category
from django import forms

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('first_name', 'last_name', 'email', 'phone', 'experience')

choices = Category.objects.all().values_list('name', 'name')

choice_list = []
for item in choices:
    choice_list.append(item)

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'description', 'snippet', 'requirement', 'workCondition', 'category', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'requirement': forms.Textarea(attrs={'class': 'form-control'}),
            'workCondition': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'description', 'snippet', 'requirement', 'workCondition', 'category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'requirement': forms.Textarea(attrs={'class': 'form-control'}),
            'workCondition': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        }