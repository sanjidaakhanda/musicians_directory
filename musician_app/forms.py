from django import forms
from .models import MusicianInfo

class MusicianForm(forms.ModelForm):
    class Meta:  
        model = MusicianInfo
        fields = '__all__'
