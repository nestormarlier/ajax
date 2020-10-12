from core.erp.models import ParteImpresion
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

class ParteImpresionListView(ListView):
    model = ParteImpresion
    template_name = 'parteimpresion/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def port(self, request, *args, **kwargs):
        data = {}
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de partes de impresión'
        return context
    