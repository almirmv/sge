from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class InflowListView(ListView):
    model = models.Inflow  # classe vai montar queryset com Inflow.objects.all()
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()    # pega a queryset criada na classe
        product = self.request.GET.get('product')  # verifica se tem busca no name
        if product:
            queryset = queryset.filter(product__title__icontains=product)
        return queryset


class InflowCreateView(CreateView):
    model = models.Inflow
    template_name = 'inflow_create.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow_list')


class InflowDetailView(DetailView):
    model = models.Inflow
    template_name = 'inflow_detail.html'


#class InflowUpdateView(UpdateView):
#    model = models.Inflow
#    template_name = 'inflow_update.html'
#    form_class = forms.InflowForm
#   success_url = reverse_lazy('inflow_list')


#class InflowDeleteView(DeleteView):
#    model = models.Inflow
#    template_name = 'inflow_delete.html'
#    success_url = reverse_lazy('inflow_list')
