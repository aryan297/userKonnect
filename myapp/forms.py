# Create your models here.

from django import forms
from .models import *


class Comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
    
class Nested_Comment_form(forms.ModelForm):
    class Meta:
        model = Nested_Comment
        fields = ['text']
