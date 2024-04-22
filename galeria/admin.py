from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id","nome","categoria","legenda","publicada") # Dados exibidos na pagina de admin
    list_display_links = ("id","nome") # Quais dados são link clicáveis
    search_fields = ("nome",) # Quais dados podem ser pesquisados na barra de pesquisa
    list_filter = ("categoria","publicada","usuario") # Filtros
    list_editable = ("publicada",) # Permite editar dado direto pela página inicial de admin sem acessar o objeto diretamente
    list_per_page = 10 # Itens exibidos por página

admin.site.register(Fotografia, ListandoFotografias) # Cria na página de admin o campo de registro e modificação da classe indicada
