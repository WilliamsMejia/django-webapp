from django import forms

from .models import recipe


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
    def clean_Title(self, *args, **kwargs):
        title = self.cleaned_data.get('Title').split()
        with open('BannedWords.txt') as file:
            contents = file.read()
            for word in title:
                if word in contents:
                    raise forms.ValidationError("Please do not use inappropriate language")
        return " ".join(title)