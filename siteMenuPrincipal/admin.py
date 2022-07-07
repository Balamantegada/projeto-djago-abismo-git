# Register your models here.
from django.contrib import admin

from siteMenuPrincipal.models import ParteInicial, BarradeNavegação, SegundaSessão, TerceiraSessão, QuartaSessão, \
    QuintaSessão, SextaSessão, SetimaSessão, OitavaSessão, NonaSessão, Rodapé, iconsQuintaSessão


@admin.register(ParteInicial)
class ParteInicial(admin.ModelAdmin):
    list_display = ('tituloInicial', 'subTituloInicial', 'imagemFundoPrincipal', 'slider1Principal', 'slider2Principal', 'criados', 'modificados', 'ativo')


@admin.register(BarradeNavegação)
class BarradeNavegação(admin.ModelAdmin):
    list_display = ('primeiraOpcao', 'segundaOpcao', 'terceiraOpcao', 'quartaOpcao', 'quintaOpcao', 'sextaOpcao',
                    'ultimoBotao', 'logoNav', 'criados', 'modificados', 'ativo')


@admin.register(SegundaSessão)
class SegundaSessão(admin.ModelAdmin):
    list_display = ('pontosTitulo', 'primeiroPonto', 'terceiroPonto', 'quintoPonto',
                    'descrisaoPontos', 'criados', 'modificados', 'ativo')


@admin.register(TerceiraSessão)
class TerceiraSessão(admin.ModelAdmin):
    list_display = ('primeiroTitulo', 'primeiraDescrisao', 'primeiroBotao', 'imagemEsquerda', 'criados', 'modificados', 'ativo')


@admin.register(QuartaSessão)
class QuartaSessão(admin.ModelAdmin):
    list_display = ('segundoTitulo', 'segundaDescrisao', 'primeiroTopico', 'segundoTopico', 'terceiroTopico', 'segundoBotao'
                    , 'imagemDireita', 'criados', 'modificados', 'ativo')


@admin.register(QuintaSessão)
class QuintaSessão(admin.ModelAdmin):
    list_display = ('subtituloSuperior', 'tituloQuintaSessao', 'descrisaoPrincipal', 'botaoQuintaSessao', 'criados',  'imagemDireita',
                    'modificados', 'ativo')

@admin.register(iconsQuintaSessão)
class iconsQuintaSessão(admin.ModelAdmin):
    list_display = ('DescrisaoIcone', 'icon', 'criados', 'modificados', 'ativo')


@admin.register(SextaSessão)
class SextaSessão(admin.ModelAdmin):
    list_display = ('tituloPrincipalSextaSessao', 'primeiroSubtituloSextaSessao', 'primeiraDescrisaoSextaSesssao',
                    'segundoSubtituloSextaSessao', 'segundaDescrisaoSextaSesssao', 'terceiroSubtituloSextaSessao',
                    'terceiraDescrisaoSextaSesssao', 'quartoSubtituloSextaSessao', 'quartaDescrisaoSextaSesssao',
                    'botaoSextaSessao', 'imagemPrincipal', 'criados', 'modificados', 'ativo')


@admin.register(SetimaSessão)
class SetimaSessão(admin.ModelAdmin):
    list_display = ('subtituloSuperiorSetimaSessao', 'tituloPrincipalSetimaSessao', 'primeiroTituloCardSetimaSessao',
                    'descrisaoPrimeiroCardSetimaSessao', 'segundoTituloCardSetimaSessao',
                    'descrisaoSegundoCardSetimaSessao',
                    'terceiroTituloCardSetimaSessao', 'descrisaoterceiroCardSetimaSessao'
                    , 'criados', 'modificados', 'ativo')


@admin.register(OitavaSessão)
class OitavaSessão(admin.ModelAdmin):
    list_display = ('subtituloSuperiorOitavaSessao', 'tituloPrincipalOitavaSessao', 'descrisaoOitavaSessao',
                    'botaoOitavaSessao', 'imagemDoVideo', 'criados', 'modificados', 'ativo')


@admin.register(NonaSessão)
class NonaSessão(admin.ModelAdmin):
    list_display = ('enderecoNonaSessao', 'numeroNonaSessao', 'emailNonaSessao', 'logoInferior', 'criados', 'modificados', 'ativo')


@admin.register(Rodapé)
class Rodapé(admin.ModelAdmin):
    list_display = ('copyrightRodape', 'nomeRodape', 'criados', 'modificados', 'ativo')

# @admin.register(Template)
# class Template(admin.ModelAdmin):
#    list_display = (,'criados', 'modificados', 'Ativo')
