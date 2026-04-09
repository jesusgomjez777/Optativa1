from django import forms
from.models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "descripcion", "precio"]
        widgets = {
            "nombre":forms.TextInput ( attrs={
                "placeholder": "Nombre del producto"
            }),
            "descripcion": forms.TextInput(attrs={
                "rows":4,
                "placeholder": "Descripcion breve"
            }),
            "precio": forms.NumberInput(attrs={
                "step": "0.01",
                "min": "0"
            }),
        }
     
     
    def clean_precio(self):
        #si el precio es negativo o cero, se lanza una excepción
        precio = self.cleaned_data.get("precio")
        if precio is not None and precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero.")
        return precio