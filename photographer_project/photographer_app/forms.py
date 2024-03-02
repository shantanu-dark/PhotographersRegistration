# photographer_app/forms.py
from django import forms
from .models import Photographer

class AddPhotographerForm(forms.ModelForm):
    class Meta:
        model = Photographer
        fields = '__all__'

class SearchPhotographerForm(forms.Form):
    search_option = forms.ChoiceField(choices=[('business_name', 'Business Name'), ('photographer_name', 'Photographer Name'), ('event', 'Event')])
    search_key = forms.CharField(max_length=255)
