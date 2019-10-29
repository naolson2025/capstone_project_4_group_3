from django import forms
from .models import RecipeSearch

class NewSearch(forms.ModelForm):
    class Meta:
        model = RecipeSearch
        fields = ('users_search',)