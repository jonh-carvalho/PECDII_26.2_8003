from django.urls import path

from .views import (
    ProdutoCreateView,
    ProdutoDeleteView,
    ProdutoDetailView,
    ProdutoListView,
    ProdutoUpdateView,
)

urlpatterns = [
    path('', ProdutoListView.as_view(), name='produto_list'),
    path('produtos/', ProdutoListView.as_view(), name='produto_list'),
    path('produtos/novo/', ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
    path('produtos/<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto_update'),
    path('produtos/<int:pk>/excluir/', ProdutoDeleteView.as_view(), name='produto_delete'),
]
