from core.erp.models import Category, Categoria, FichaTecnica, Operario, Impresora, Parada, CambioMecanico
from django.forms import *

from django.contrib.admin import widgets

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

class FichaTecnicaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = FichaTecnica
        fields = ['nombre', 'user']
        exclude = ['id','active','created','modified', 'delete']
        widgets = {
            'nombre' : TextInput(
                attrs={
                    'placeholder' : 'Ingrese nombre'
                }
            )
        }

class OperarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class']= 'form-control'
            form.field.widget.attrs['autocomplete']= 'off'
        self.fields['legajo'].widget.attrs['autofocus']=True
    class Meta:
        model = Operario
        fields = '__all__'
        exclude = ['activo','modified','delete']

class ImpresoraForm(ModelForm): 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class']= 'form-control'
            form.field.widget.attrs['autocomplete']= 'off'
        self.fields['impresora_id'].widget.attrs['autofocus']= True
    
    class Meta:
        model = Impresora
        fields = '__all__'
        exclude = ['created', 'modified', 'activo', 'delete']

        widgets={
            'impresora_id': NumberInput(
                attrs={
                    'placeholder':'Ingrese número de impresora'
                }
            ),
            'nombre':TextInput(
                attrs={
                    'placeholder':'Ingrese nombre de la impresora'
                }
            )
        }

class ParadaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class']= 'form-control'
            form.field.widget.attrs['autocomplete']= 'off'
        self.fields['nombre'].widget.attrs['autofocus']= True
    class Meta:
        model = Parada
        fields = '__all__'
        exclude = ['created', 'modified','active', 'delete']
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre de parada de máquina'
                }
            ),
            'sector_asignado': Select (
                attrs={
                    'placeholder': 'Ingrese a que sector implica la parada de máquina'
                }
            )
        }

class CambioMecanicoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CambioMecanicoForm, self).__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
            self.fields['create'].widget.attrs['readonly'] = True
            self.fields['fecha_fin'].widget = widgets.AdminSplitDateTime()
            self.fields['parada'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = CambioMecanico
        fields = '__all__'
        exclude = ['id', 'modified']