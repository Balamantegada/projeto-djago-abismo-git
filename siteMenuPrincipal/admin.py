# Register your models here.
from django.contrib import admin

from siteMenuPrincipal.models import PaginaInicial


@admin.register(PaginaInicial)
class PaginaInicial(admin.ModelAdmin):
    list_display = ('tituloInicial', 'subTituloInicial',

                    'primeiraOpcao', 'segundaOpcao', 'terceiraOpcao', 'quartaOpcao', 'quintaOpcao', 'sextaOpcao',
                    'ultimoBotao',

                    'pontosTitulo', 'primeiroPonto', 'terceiroPonto', 'quintoPonto',
                    'descrisaoPontos', 'primeiroTitulo', 'primeiraDescrisao', 'primeiroBotao',
                    'segundoTitulo', 'segundaDescrisao', 'primeiroTopico', 'segundoTopico', 'terceiroTopico', 'segundoBotao',

                    'subtituloSuperior', 'tituloQuintaSessao', 'descrisaoPrincipal', 'botaoQuintaSessao',
                    'primeiraDescrisaoIcone', 'segundaDescrisaoIcone', 'terceiraDescrisaoIcone', 'quartaDescrisaoIcone',
                    'quintaDescrisaoIcone',

                    'tituloPrincipalSextaSessao', 'primeiroSubtituloSextaSessao', 'primeiraDescrisaoSextaSesssao',
                    'segundoSubtituloSextaSessao', 'segundaDescrisaoSextaSesssao', 'terceiroSubtituloSextaSessao',
                    'terceiraDescrisaoSextaSesssao', 'quartoSubtituloSextaSessao', 'quartaDescrisaoSextaSesssao',
                    'botaoSextaSessao',

                    'subtituloSuperiorSetimaSessao', 'tituloPrincipalSetimaSessao', 'primeiroTituloCardSetimaSessao',
                    'descrisaoPrimeiroCardSetimaSessao', 'segundoTituloCardSetimaSessao', 'descrisaoSegundoCardSetimaSessao',
                    'terceiroTituloCardSetimaSessao', 'descrisaoterceiroCardSetimaSessao',

                    'subtituloSuperiorOitavaSessao', 'tituloPrincipalOitavaSessao', 'descrisaoOitavaSessao',
                    'botaoOitavaSessao',

                    'enderecoNonaSessao', 'numeroNonaSessao', 'emailNonaSessao',

                    'copyrightRodape', 'nomeRodape',

                    'criados', 'modificados', 'ativo')
