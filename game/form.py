from django import forms
from .models import app


class subjectsForm(forms.ModelForm):
    class Meta:
        model = app
        fields = "__all__"