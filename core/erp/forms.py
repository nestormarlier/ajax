from core.erp.models import Category, Categoria
from django.forms import *

class CategoryForm(ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre'
                }
            )
        }

class CategoriaForm(ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class']= 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus']= True
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'id_jefe']
        exclude = ['created', 'modified']
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre'
                }
            ),
            'id_jefe': TextInput(
                attrs={
                    'placeholder': 'Ingrese identificacion del jefe'
                }
            )
        }
