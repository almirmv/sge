from django.urls import path
from . import views

urlpatterns = [
    path('outflows/list/', views.OutflowListView.as_view(), name='outflow_list'),
    path('outflows/create/', views.OutflowCreateView.as_view(), name='outflow_create'),
    path('outflows/<int:pk>/detail/', views.OutflowDetailView.as_view(), name='outflow_detail'),
    # nao sera criado alterar e deletar. So adm no django admin podera fazer isso
    #path('outflows/<int:pk>/update/', views.InflowUpdateView.as_view(), name='outflow_update'),
    #path('outflows/<int:pk>/delete/', views.InflowDeleteView.as_view(), name='outflow_delete'),
]
