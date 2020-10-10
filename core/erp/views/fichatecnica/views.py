from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from core.erp.models import FichaTecnica


def fichatecnica_list(request):
    data = {
        'title': 'Listado de Fichas Técnicas',
        'categories': FichaTecnica.objects.all()
    }
    return render(request, 'fichatecnica/listfunction.html', data)


class FichaTecnicaListView(ListView):
    model = FichaTecnica
    template_name = 'fichatecnica/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = FichaTecnica.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Fichas Técnicas'
        return context