from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Enter article title'})
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter article content'})
    )

    class Meta:
        model = Article
        fields = ['title', 'content']