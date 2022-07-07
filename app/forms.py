from django import forms
from .models import Cliente , Encomienda , Seguimiento



class Clienteform(forms.ModelForm):
    class Meta:
        model=Cliente
        fields='__all__'


class IngresoForm(forms.ModelForm):
    class Meta:
        model=Encomienda
        exclude=['cliente','num_env']
        
class SegForm(forms.ModelForm):
    class Meta:
        model=Seguimiento
        fields=['codigo']
        