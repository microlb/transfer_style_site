from django import forms

class PictureForm(forms.Form):
    content = forms.ImageField()
    style = forms.ImageField()
