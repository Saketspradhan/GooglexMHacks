from django import forms
from .models import SurveyAnswers

class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyAnswers
        fields = ['destination', 'trip_length', 'group_size', 'pace', 'budget']
from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()