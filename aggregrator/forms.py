from django import forms
from .models import Search

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = [
            'search_indonesian',
            'search_english',            
        ]

        widgets = {
            'search_indonesian': forms.TextInput(attrs= { 'class': 'form-control'} ),
            'search_english': forms.TextInput(attrs= { 'class': 'form-control'} )
        }
