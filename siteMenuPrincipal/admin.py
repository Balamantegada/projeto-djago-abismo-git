# Register your models here.
from django.contrib import admin

from siteMenuPrincipal.models import ParteInicial, BarradeNavegação, SegundaSessão, TerceiraSessão, QuartaSessão, \
    QuintaSessão, SextaSessão, SetimaSessão, OitavaSessão, NonaSessão, Rodapé


@admin.register(ParteInicial)
class ParteInicial(admin.ModelAdmin):
    list_display = ('tituloInicial', 'subTituloInicial')


@admin.register(BarradeNavegação)
class BarradeNavegação(admin.ModelAdmin):
    list_display = ('primeiraOpcao', 'segundaOpcao', 'terceiraOpcao', 'quartaOpcao', 'quintaOpcao', 'sextaOpcao',
                    'ultimoBotao')


@admin.register(SegundaSessão)
class SegundaSessão(admin.ModelAdmin):
    list_display = ('pontosTitulo', 'primeiroPonto', 'terceiroPonto', 'quintoPonto',
                    'descrisaoPontos')


@admin.register(TerceiraSessão)
class TerceiraSessão(admin.ModelAdmin):
    list_display = ('primeiroTitulo', 'primeiraDescrisao', 'primeiroBotao')


@admin.register(QuartaSessão)
class QuartaSessão(admin.ModelAdmin):
    list_display = ('segundoTitulo', 'segundaDescrisao', 'primeiroTopico', 'segundoTopico', 'terceiroTopico', 'segundoBotao')


@admin.register(QuintaSessão)
class QuintaSessão(admin.ModelAdmin):
    list_display = ('subtituloSuperior', 'tituloQuintaSessao', 'descrisaoPrincipal', 'botaoQuintaSessao',
                    'primeiraDescrisaoIcone', 'segundaDescrisaoIcone', 'terceiraDescrisaoIcone', 'quartaDescrisaoIcone',
                    'quintaDescrisaoIcone')


@admin.register(SextaSessão)
class SextaSessão(admin.ModelAdmin):
    list_display = ('tituloPrincipalSextaSessao', 'primeiroSubtituloSextaSessao', 'primeiraDescrisaoSextaSesssao',
                    'segundoSubtituloSextaSessao', 'segundaDescrisaoSextaSesssao', 'terceiroSubtituloSextaSessao',
                    'terceiraDescrisaoSextaSesssao', 'quartoSubtituloSextaSessao', 'quartaDescrisaoSextaSesssao',
                    'botaoSextaSessao')


@admin.register(SetimaSessão)
class SetimaSessão(admin.ModelAdmin):
    list_display = ('subtituloSuperiorSetimaSessao', 'tituloPrincipalSetimaSessao', 'primeiroTituloCardSetimaSessao',
                    'descrisaoPrimeiroCardSetimaSessao', 'segundoTituloCardSetimaSessao',
                    'descrisaoSegundoCardSetimaSessao',
                    'terceiroTituloCardSetimaSessao', 'descrisaoterceiroCardSetimaSessao')


@admin.register(OitavaSessão)
class OitavaSessão(admin.ModelAdmin):
    list_display = ('subtituloSuperiorOitavaSessao', 'tituloPrincipalOitavaSessao', 'descrisaoOitavaSessao',
                    'botaoOitavaSessao')


@admin.register(NonaSessão)
class NonaSessão(admin.ModelAdmin):
    list_display = ('enderecoNonaSessao', 'numeroNonaSessao', 'emailNonaSessao')


@admin.register(Rodapé)
class Rodapé(admin.ModelAdmin):
    list_display = ('copyrightRodape', 'nomeRodape')

# @admin.register(Template)
# class Template(admin.ModelAdmin):
#    list_display = (,'criados', 'modificados', 'Ativo')
