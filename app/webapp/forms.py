from django import forms
from webapp.models import Image



class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'sign')