from core.erp.models import Categoria
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator


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
    
    

