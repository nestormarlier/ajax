from django.urls import path
from core.erp.views.category.views import *
from core.erp.views.fichatecnica.views import *
from core.erp.views.categoria.views import *
from core.erp.views.operario.views import *
from core.erp.views.impresora.views import *
from core.erp.views.parteimpresion.views import *
from core.erp.views.parada.views import *
from core.erp.views.cambiomecanico.views import *
from core.erp.views.setup.views import *
from core.erp.views.produccion.views import *

app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/list2/', category_list, name='category_list2'),
    path('fichatecnicaxfuncion/list/', fichatecnica_list, name='fichatecnica_list_x_funcion'),
    path('fichatecnica/list/', FichaTecnicaListView.as_view(), name='fichatecnica_list'),
    path('categoria/list/', CategoriaListView.as_view(), name='categoria_list'),
    path('operario/list/', OperarioListView.as_view(), name='operario_list'), 
    path('impresora/list/', ImpresoraListView.as_view(), name="impresora_list"),
    path('parada/list/', ParadaListView.as_view(), name='parada_list'),
    path('cambiomecanico/list/', CambioMecanicoListView.as_view(), name='cambiomecanico_list'),
    path('setup/list/', SetupListView.as_view(), name='setup_list'),
    path('produccion/list/', ProduccionListView.as_view(), name='produccion_list'),
    path('parteimpresion/list/', ParteImpresionListView.as_view(), name="parteimpresion_list"),
    ### ALTAS ###
    path('category/alta/', CategoryCreateView.as_view(), name="category_create"),
    path('categoria/alta/', CategoriaCreateView.as_view(), name="categoria_create"),
]