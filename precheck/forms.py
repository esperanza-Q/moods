from django import forms
from .models import Checkpost
from django.forms import TextInput, NumberInput,Textarea

class Checkpostform(forms.ModelForm):
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True, empty_label=None)
    class Meta:
        model=Checkpost
        fields=['content']
        
    checkimage = forms.ImageField(required=True)
    widgets = {
        'content': Textarea(attrs={
                'class': "form-control",
                'style': 'width: 500px; height: 500px;'
                # 'placeholder': 'Age'
            }),
    }