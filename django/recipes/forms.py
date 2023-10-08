from django import forms

from .models import recipe
from profanity_filter import ProfanityFilter
import spacy
class RecipeForm(forms.ModelForm):
    Title = forms.CharField(widget = forms.TextInput(attrs={"placeholder": "Your Title"}))
    class Meta:
        model = recipe
        fields = [
        'Title',
        'Cooking_Time',
        'Serving_Size',
        'Ingredients',
        'Directions'
        ]

    def clean_Title(self, *args, **kwargs): #Very simple profanity filter to check for banned words and change then to ****
        
        title = self.cleaned_data.get('Title')
        with open('BannedWords.txt') as file:
                contents = file.read()
                for word in contents:
                        title = title.replace(word, '*' * len(word))
                return title
