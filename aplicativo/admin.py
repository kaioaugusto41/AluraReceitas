from django.contrib import admin
from .models import Receita



class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria')
    list_display_links = ('id', 'nome')

admin.site.register(Receita, ListandoReceitas)

