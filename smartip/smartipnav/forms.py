from django import forms

class UsersPcForm(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    nombre_usuario_pc = forms.CharField()
    nombre_pc = forms.CharField()