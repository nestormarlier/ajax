from core.erp.models import Categoria
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator

from django.urls import reverse_lazy

from core.erp.forms import CategoriaForm


class CategoriaListView(ListView):
    model = Categoria
    template_name = "categoria/list.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Categoria.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de categorías'
        context["entidad"] = 'Categoría'
        context["list_url"] = reverse_lazy('erp:categoria_list')
        context["create_url"] = reverse_lazy('erp:categoria_create')
        return context


class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "categoria/create.html"
    success_url = reverse_lazy('erp:categoria_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Creación de una categoría'
        context["entidad"] = 'Categoría'
        context["list_url"] = reverse_lazy('erp:categoria_list')


        return context
    