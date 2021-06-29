from django import forms
from .models import Ad
  
  
class AdForm(forms.ModelForm):
    title = forms.CharField(label='Название', required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={"class":"form-control"}))
    price = forms.CharField(label='Стоимость', widget=forms.TextInput(attrs={"class":"form-control", 'type':'number'}))
    geo = forms.CharField(label='Местоположение', widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model = Ad
        fields = [
            "title",
            "description",
            "price",
            "geo"
        ]
       