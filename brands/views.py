from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'brands.view_brand'  # app.action_model
    model = models.Brand  # classe vai montar queryset com Brand.objects.all()
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()    # pega a queryset criada na classe
        name = self.request.GET.get('name')  # verifica se tem busca no name
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'brands.add_brand'
    model = models.Brand
    template_name = 'brand_create.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand_list')


class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'brands.view_brand'
    model = models.Brand
    template_name = 'brand_detail.html'


class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'brands.change_brand'
    model = models.Brand
    template_name = 'brand_update.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand_list')


class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'brands.delete_brand'
    model = models.Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brand_list')
