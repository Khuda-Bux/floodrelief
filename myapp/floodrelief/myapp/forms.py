from django import forms
from .models import Relief
#from django.contrib.auth.forms import AuthenticationForm,UsernameField
#from django.utils.translation import gettext_lazy as _
class ReliefForm(forms.ModelForm):
 #class LoginForm(AuthenticationForm):
    #username=UsernameField(widget=forms.TextInput(attrs=
    #{'autofocus': True, 'class':'form-control'}))
    #password= forms.CharField(
          # label=('Password'),
           #strip=False,
           #widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
            #'class':'form-control'}),)
            
          

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
