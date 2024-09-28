from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers
from app.metrics import get_sales_metrics


class OutflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'outflows.view_outflow'  # app.action_model
    model = models.Outflow  # classe vai montar queryset com Outflow.objects.all()
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()    # pega a queryset criada na classe
        product = self.request.GET.get('product')  # verifica se tem busca no product
        if product:
            queryset = queryset.filter(product__title__icontains=product)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    # contexto atual
        context['sales_metrics'] = get_sales_metrics()  # injeta sales metrics
        return context

class OutflowCreateView(LoginRequiredMixin, PermissionRequiredMixin,  CreateView):
    permission_required = 'outflows.add_outflow'
    model = models.Outflow
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list')


class OutflowDetailView(LoginRequiredMixin, PermissionRequiredMixin,  DetailView):
    permission_required = 'outflows.view_outflow'
    model = models.Outflow
    template_name = 'outflow_detail.html'


#class OutflowUpdateView(UpdateView):
#    model = models.Outflow
#    template_name = 'outflow_update.html'
#    form_class = forms.OutflowForm
#   success_url = reverse_lazy('outflow_list')


#class OutflowDeleteView(DeleteView):
#    model = models.Outflow
#    template_name = 'outflow_delete.html'
#    success_url = reverse_lazy('outflow_list')


class OutflowCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Outflow.objects.all()
    serializer_class = serializers.OutflowSerializer


class OutflowRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Outflow.objects.all()
    serializer_class = serializers.OutflowSerializer