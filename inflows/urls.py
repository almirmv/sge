from django.urls import path
from . import views

urlpatterns = [
    path('inflows/list/', views.InflowListView.as_view(), name='inflow_list'),
    path('inflows/create/', views.InflowCreateView.as_view(), name='inflow_create'),
    path('inflows/<int:pk>/detail/', views.InflowDetailView.as_view(), name='inflow_detail'),
    # nao sera criado alterar e deletar. So adm no django admin podera fazer isso
    #path('inflows/<int:pk>/update/', views.InflowUpdateView.as_view(), name='inflow_update'),
    #path('inflows/<int:pk>/delete/', views.InflowDeleteView.as_view(), name='inflow_delete'),
]
