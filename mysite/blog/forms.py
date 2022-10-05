from django import forms
from .models import Comment, UserEmails


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['time_create', 'post']
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': 'Write Your Comments...', 'cols': 100}),
            'website': forms.URLInput(attrs={'placeholder': 'Website'}),
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }


class UserEmailsForm(forms.ModelForm):
    class Meta:
        model = UserEmails
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address *'}),
        }