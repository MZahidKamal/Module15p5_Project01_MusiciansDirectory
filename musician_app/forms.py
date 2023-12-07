from django import forms
from .models import Musician_Model

class MusicianModel_Form(forms.ModelForm):
    class Meta:
        model = Musician_Model
        fields = '__all__'
