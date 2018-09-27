from django import forms
from blog.models import *

class UserForm(forms.ModelForm):
    username = forms.CharField(label='用户名',required=True)
    headimg = forms.FileField(required=False)
    password = forms.CharField(label='密码',required=True,widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = '__all__'