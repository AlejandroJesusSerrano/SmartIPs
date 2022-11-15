from django import forms

class UsersPcForm(forms.Form):

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-light'}))
    apellido = forms.CharField()
    nombre_usuario_pc = forms.CharField()
    nombre_pc = forms.CharField()