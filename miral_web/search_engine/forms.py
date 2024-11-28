from django import forms
from .models import Article

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['url', 'title', 'description']
