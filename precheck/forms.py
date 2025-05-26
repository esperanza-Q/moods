from django import forms
from .models import Checkpost
from django.forms import TextInput, NumberInput,Textarea

class Checkpostform(forms.ModelForm):
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True, empty_label=None)
    checkimage = forms.ImageField(required=True)
    
    class Meta:
        model = Checkpost
        fields = ['content']
        widgets = {
            'content': Textarea(attrs={
                'class': "form-control",
                # 'style': 'width: 500px; height: 500px;',
                'placeholder': """작성된 인증글이 없습니다. 인증글을 작성해주세요
(인증글 작성 시 가이드글과 예시 작성문을 삭제 후 양식에 맞추어 재작성해주시면 됩니다)

<인증 가이드>
학번 / 성명 / 가입 시 사용한 이메일
학교이름, 성명, 학번이 보이는 학생증 사진

Ex) 20240000 / 김수정 / moodsncafe@naver.com"""
            }),
        }
