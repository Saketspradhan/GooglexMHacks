from django import forms
from .models import SurveyAnswers

class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyAnswers
        fields = ['destination', 'trip_length', 'group_size', 'pace', 'budget']
