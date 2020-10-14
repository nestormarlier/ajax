from core.erp.models import Categoria
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator

from core.erp.forms import CategoriaForm
from django.urls import reverse_lazy


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
        return context


class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "categoria/create.html"
    success_url = reverse_lazy('erp:categoria_list')

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Creación de categoría"
        return context
