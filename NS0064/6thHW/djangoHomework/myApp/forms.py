from django import forms
from .models import Blog

class blogForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter blog title'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter blog description'})
    )
    class Meta:
        model = Blog
        fields = ['title', 'description']