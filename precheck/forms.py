from django import forms
from .models import Checkpost
from django.forms import TextInput, NumberInput,Textarea

class Checkpostform(forms.ModelForm):
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True, empty_label=None)
    class Meta:
        model=Checkpost
        fields=['content']
        
    checkimage = forms.ImageField(required=True)
        # widgets = {
        #     'title': TextInput(attrs={
        #         'class': "form-control",
        #         'style': 'max-width: 300px;'
        #         # 'placeholder': 'Name'
        #         }),
        # }