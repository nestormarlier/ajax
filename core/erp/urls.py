from django.urls import path
from core.erp.views.category.views import *
from core.erp.views.fichatecnica.views import *
from core.erp.views.categoria.views import *
from core.erp.views.operario.views import *
from core.erp.views.impresora.views import *

app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/list2/', category_list, name='category_list2'),
    path('fichatecnicaxfuncion/', fichatecnica_list, name='fichatecnica_list_x_funcion'),
    path('fichatecnica/', FichaTecnicaListView.as_view(), name='fichatecnica_list'),
    path('categoria/', CategoriaListView.as_view(), name='categoria_list'),
    path('operario/', OperarioListView.as_view(), name='operario_list'), 
    path('impresora/', ImpresoraListView.as_view(), name="impresora_list"),
    path('category/alta/', CategoryCreateView.as_view(), name='category_create')
]
