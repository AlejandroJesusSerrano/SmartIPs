from django import forms

#*IP Form Model
class IpForm(forms.Form):

    direccion_ip = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mx-auto w-90'}))
    equipo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mx-auto w-90'}))
    internet_acceso_libre = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    
#*Users PC Form Model
class UsersPcForm(forms.Form):

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mx-auto w-90'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mx-auto w-90'}))
    nombre_usuario_pc = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mx-auto w-90'}))
    nombre_pc = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mx-auto w-90'}))

#*Offices Form Model
class OfficeForm(forms.Form):
    oficina = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mx-auto w-90'}))
    piso = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mx-auto w-90'}))
    juzgado = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mx-auto w-90'}))
    edificio = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mx-auto w-90'}))
