from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator

from core.erp.models import Category
from core.erp.forms import CategoryForm

def category_list(request):
    data = {
        'title': 'Listado de Categorías',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)

class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Category.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        context['create_url'] = reverse_lazy('erp:category_create')
        context['entidad'] = 'Category'
        #context['list_url'] = reverse_lazy('erp:category_list')
        return context

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('erp:category_list')

    def post(self,request, *args , **kwargs):
        data = {}
        action = request.POST['accion']
        try:
            if action == 'add':
                #form = CategoryForm(request.POST)
                form = self.get_form() #con esta propiedad obtengo todos los datos enviado, inclusive si son imagenes
                if form.is_valid():
                    form.save()
                else:
                    data = form.errors
            else:
                data['error'] = 'No ha ingresado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    #     print(request.POST)

    #     #a nuestro formulario CategoryForm le asigno lo que trae el POST y se lo asigno a la variable
    #     formulario = CategoryForm(request.POST)
    #     if formulario.is_valid():
    #         formulario.save()
    #         return HttpResponseRedirect(self.success_url)
    #     print(formulario.errors)
    #     self.object = None
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = formulario
    #     return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Creación de una categoría'
        context["entidad"] = 'Category'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['accion'] = 'add'
        return context
    