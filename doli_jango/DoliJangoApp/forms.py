from django import forms
from django.forms import inlineformset_factory, modelformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tercero
from .models import Empresa

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        
         
    
class TerceroForm(forms.ModelForm):
    class Meta:
        model = Tercero
        fields = '__all__'
        
class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        

    def __init__(self, *args, **kwargs):
        super(TerceroForm, self).__init__(*args, **kwargs)
        
