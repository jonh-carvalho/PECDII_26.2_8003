from django.contrib import admin

from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'estoque', 'disponivel')
    list_filter = ('disponivel', 'categoria')
    search_fields = ('nome', 'descricao', 'categoria')
