from django import forms
from .models import Album_Model

class AlbumModel_Form(forms.ModelForm):
    class Meta:
        model = Album_Model
        fields = '__all__'
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }
