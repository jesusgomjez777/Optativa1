from django import forms
from django.forms import inlineformset_factory
from.models import Producto, Cliente, Pedido, PedidoItem

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


class PedidoSimpleForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["cliente", "estado"]
      
class PedidoItemForm(forms.ModelForm):
    class Meta:
        model = PedidoItem
        fields = ["pedido", "producto", "cantidad", "precio_unitario"]
        widgets = {
            "cantidad": forms.NumberInput(attrs={"min": "1", "step": "1",}),
            "precio_unitario": forms.NumberInput(attrs={"min": "0", "step": "0.01",}),
        }

PedidoItemFormSet = inlineformset_factory(
    parent_model=Pedido,
    model=PedidoItem,
    form=PedidoItemForm,
    extra=1, #cuantas filas vacias mostrar por defecto
    can_delete=True #permitir eliminar filas
)

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"