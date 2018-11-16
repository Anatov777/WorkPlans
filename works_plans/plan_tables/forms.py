from django import forms
from .models import *
from django.forms import formset_factory

class PlansFallForm(forms.ModelForm):

    class Meta:
        model = plansFall
        exclude = [""]

class ColorForm(forms.Form):
    color = forms.ChoiceField(choices=(('blue', 'Blue'), ('red', 'Red')))
