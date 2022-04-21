from django import forms
from django.forms import ModelForm
from .models import UserInfo,pdf
from django import forms

class UserForm(ModelForm): # model form will directly make changes to database instad of creating any duplicates.
    class Meta:
        model= UserInfo
        fields = '__all__'
        
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)


class PdfForm(ModelForm):
    class Meta:
        model= pdf
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PdfForm, self).__init__(*args, **kwargs)
