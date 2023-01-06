from django import forms
from .models import Relief

class ReliefForm(forms.ModelForm):
   class Meta:
     model = Relief
     fields = ['id','name','nic','district','tehsil','uc','mobile_number','photo','date']
     widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
     'nic':forms.NumberInput(attrs={'class':'form-control type="text" placeholder="Disabled input" aria-label="Disabled input example" disabled'}),
     'district':forms.TextInput(attrs={'class':'form-control'}),
     'tehsil':forms.TextInput(attrs={'class':'form-control'}),
     'uc':forms.TextInput(attrs={'class':'form-control'}),
     'mobile_number':forms.NumberInput(attrs={'class':'form-control'}),
     'photo':forms.FileInput(attrs={'class':'form-control'}),
     'date':forms.TextInput(attrs={'class':'form-control'}),
     }
