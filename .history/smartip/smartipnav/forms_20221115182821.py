from django import forms

class UsersPcForm(forms.Form):

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mx-auto w-90'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mx-auto w-90'}))
    nombre_usuario_pc = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mx-auto w-90'}))
    nombre_pc = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mx-auto w-90'}))
