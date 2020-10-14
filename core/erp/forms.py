from django.forms import *
from core.erp.models import Category, Categoria

class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocmplete'] = 'off'
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name' : TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre',
                }
            )
        }

class CategoriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocmplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True        

    class Meta:
        model = Categoria
        fields = ['nombre', 'id_jefe']
        exclude = ['id','created', 'modified']
        widgets = {
            'nombre' : TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre',
                }
            ),
            'id_jefe' : TextInput(
                attrs={
                    'placeholder' : 'Ingrese Id del jefe'
                }
            )
        }