from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Produto


class ProdutoListView(ListView):
    model = Produto
    template_name = 'catalogo/produto_list.html'
    context_object_name = 'produtos'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        termo = self.request.GET.get('q')
        if termo:
            return queryset.filter(
                Q(nome__icontains=termo) |
                Q(descricao__icontains=termo) |
                Q(categoria__icontains=termo)
            )
        return queryset


class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'catalogo/produto_detail.html'
    context_object_name = 'produto'


class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'catalogo/produto_form.html'
    fields = ['nome', 'descricao', 'preco', 'estoque', 'categoria', 'disponivel']
    success_url = reverse_lazy('produto_list')


class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'catalogo/produto_form.html'
    fields = ['nome', 'descricao', 'preco', 'estoque', 'categoria', 'disponivel']
    success_url = reverse_lazy('produto_list')


class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'catalogo/produto_confirm_delete.html'
    success_url = reverse_lazy('produto_list')
