from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class SupplierListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'suppliers.view_supplier'  # app.action_model
    model = models.Supplier  # classe vai montar queryset com Supplier.objects.all()
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()    # pega a queryset criada na classe
        name = self.request.GET.get('name')  # verifica se tem busca no name
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class SupplierCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'suppliers.add_supplier'
    model = models.Supplier
    template_name = 'supplier_create.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier_list')


class SupplierDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'suppliers.view_supplier'
    model = models.Supplier
    template_name = 'supplier_detail.html'


class SupplierUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'suppliers.change_supplier'
    model = models.Supplier
    template_name = 'supplier_update.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier_list')


class SupplierDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'suppliers.delete_supplier'
    model = models.Supplier
    template_name = 'supplier_delete.html'
    success_url = reverse_lazy('supplier_list')
