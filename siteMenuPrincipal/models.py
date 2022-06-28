from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from stdimage import StdImageField


# Create your models here.
class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificados = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class ParteInicial(Base):
    tituloInicial = models.CharField('titulo (sessão 1)', max_length=100, blank=True)
    subTituloInicial = models.CharField('SubTítulo', max_length=100, blank=True)
    imagemFundoPrincipal = StdImageField('imagemFundoImagem de fundo principal', variations={'thumbnail': {'width': 1920, 'height': 1150 , 'crop': True}}, upload_to='imgs inciais', blank=True)
    slider1Principal = StdImageField('imagemFundoImagem da primeira caixa flutuante', variations={'thumbnail': {'width': 405, 'height': 239 , 'crop': True}}, upload_to='imgs inciais', blank=True)
    slider2Principal = StdImageField('imagemFundoImagem da segunda caixa flutuante', variations={'thumbnail': {'width': 285, 'height': 240 , 'crop': True}}, upload_to='imgs inciais', blank=True)

    class Meta:
        verbose_name = 'ParteInicial'
        verbose_name_plural = 'PartesIniciais'

        def __str__(self):
            return self.ParteInicial


class BarradeNavegação(Base):
    primeiraOpcao = models.CharField('1º (Barra de navegação)', max_length=100, blank=True)
    segundaOpcao = models.CharField('2º', max_length=100, blank=True)
    terceiraOpcao = models.CharField('3º', max_length=100, blank=True)
    quartaOpcao = models.CharField('4º', max_length=100, blank=True)
    quintaOpcao = models.CharField('5º', max_length=100, blank=True)
    sextaOpcao = models.CharField('6º', max_length=100, blank=True)
    ultimoBotao = models.CharField('7º', max_length=100, blank=True)
    logoNav = StdImageField('Logo da barra de navegação', variations={'thumbnail': {'width': 166, 'height': 87 , 'crop': True}}, upload_to='logo', blank=True)

    class Meta:
        verbose_name = 'BarradeNavegação'
        verbose_name_plural = 'BarrasdeNavegações'

        def __str__(self):
            return self.BarradeNavecacão


class SegundaSessão(Base):
    pontosTitulo = models.CharField('Pontos titulo (sessão 2)', max_length=100, blank=True)
    primeiroPonto = models.CharField('Primeiro ponto', max_length=100, blank=True)
    terceiroPonto = models.CharField('Segundo ponto', max_length=100, blank=True)
    quintoPonto = models.CharField('Quinto ponto', max_length=100, blank=True)
    descrisaoPontos = RichTextUploadingField('Descrisão dos pontos', blank=True)

    class Meta:
        verbose_name = 'SegundaSessão'
        verbose_name_plural = 'SegundaSessão'

        def __str__(self):
            return self.SegundaSessão


class TerceiraSessão(Base):
    primeiroTitulo = models.CharField('Primeiro titulo (sessão 3)', max_length=100, blank=True)
    primeiraDescrisao = models.CharField('Primeira descrisão', max_length=800, blank=True)
    primeiroBotao = models.CharField('Primeiro botão', max_length=80, blank=True)
    imagemEsquerda = StdImageField('Imagem na esquerda', variations={'thumbnail': {'width': 960, 'height': 800 , 'crop': True}}, upload_to='sessao3', blank=True)

    class Meta:
        verbose_name = 'TerceiraSessão'
        verbose_name_plural = 'TerceiraSessão'

        def __str__(self):
            return self.TerceiraSessão


class QuartaSessão(Base):
    segundoTitulo = models.CharField('Segundo titulo (sessão 4)', max_length=100, blank=True)
    segundaDescrisao = models.CharField('Segunda descrisão', max_length=800, blank=True)
    primeiroTopico = models.CharField('Primeiro tópico', max_length=100, blank=True)
    segundoTopico = models.CharField('Segundo tópico', max_length=100, blank=True)
    terceiroTopico = models.CharField('Terceiro tópico', max_length=100, blank=True)
    segundoBotao = models.CharField('Segundo botão', max_length=80, blank=True)
    imagemDireita = StdImageField('Imagem na direita', variations={'thumbnail': {'width': 960, 'height': 800 , 'crop': True}}, upload_to='sessao4',blank=True)

    class Meta:
        verbose_name = 'QuartaSessão'
        verbose_name_plural = 'QuartaSessão'

        def __str__(self):
            return self.QuartaSessão


class QuintaSessão(Base):
    subtituloSuperior = models.CharField('Subtitulo superior (sessão 5)', max_length=100, blank=True)
    tituloQuintaSessao = models.CharField('Titulo', max_length=100, blank=True)
    descrisaoPrincipal = RichTextUploadingField('Descrisão principal', max_length=800, blank=True)
    botaoQuintaSessao = models.CharField('Botão principal', max_length=100, blank=True)
    imagemDireita = StdImageField('Imagem na direita', variations={'thumbnail': {'width': 780, 'height': 1020 , 'crop': True}}, upload_to='sessao5', blank=True)

    class Meta:
        verbose_name = 'QuintaSessão'
        verbose_name_plural = 'QuintaSessão'

        def __str__(self):
            return self.QuintaSessão

class iconsQuintaSessão(Base):
    icon1 = StdImageField('Primeiro icone', variations={'thumbnail': {'width': 512, 'height': 512, 'crop': True}},
                          upload_to='icons', blank=True)
    primeiraDescrisaoIcone = models.CharField('Descrisão primeiro icone', max_length=250, blank=True)
    icon2 = StdImageField('Segundo icone', variations={'thumbnail': {'width': 512, 'height': 512, 'crop': True}},
                          upload_to='icons', blank=True)
    segundaDescrisaoIcone = models.CharField('Descrisão segundo icone', max_length=250, blank=True)
    icon3 = StdImageField('Terceiro icone', variations={'thumbnail': {'width': 512, 'height': 512, 'crop': True}},
                          upload_to='icons', blank=True)
    terceiraDescrisaoIcone = models.CharField('Descrisão terceiro icone', max_length=250, blank=True)
    icon4 = StdImageField('Quarto icone', variations={'thumbnail': {'width': 512, 'height': 512, 'crop': True}},
                          upload_to='icons', blank=True)
    quartaDescrisaoIcone = models.CharField('Descrisão quarto icone', max_length=250, blank=True)
    icon5 = StdImageField('Quinto icone', variations={'thumbnail': {'width': 512, 'height': 512, 'crop': True}},
                          upload_to='icons', blank=True)
    quintaDescrisaoIcone = models.CharField('Descrisão quinto icone', max_length=250, blank=True)


    class Meta:
        verbose_name = 'iconsQuintaSessão'
        verbose_name_plural = 'iconsQuintaSessão'

        def __str__(self):
            return self.iconsQuintaSessão


class SextaSessão(Base):
    tituloPrincipalSextaSessao = models.CharField('Titulo principal (sesssão 6)', max_length=100, blank=True)
    primeiroSubtituloSextaSessao = models.CharField('Primeiro subtitulo', max_length=100, blank=True)
    primeiraDescrisaoSextaSesssao = models.CharField('Primeira descrisão', max_length=400, blank=True)
    segundoSubtituloSextaSessao = models.CharField('Segundo subtitulo', max_length=100, blank=True)
    segundaDescrisaoSextaSesssao = models.CharField('Segunda descrisão', max_length=400, blank=True)
    terceiroSubtituloSextaSessao = models.CharField('Terceiro subtitulo', max_length=100, blank=True)
    terceiraDescrisaoSextaSesssao = models.CharField('Terceira descrisão', max_length=400, blank=True)
    quartoSubtituloSextaSessao = models.CharField('Quarto subtitulo', max_length=100, blank=True)
    quartaDescrisaoSextaSesssao = models.CharField('Quarta descrisão', max_length=400, blank=True)
    botaoSextaSessao = models.CharField('Botão', max_length=80, blank=True)
    imagemPrincipal = StdImageField('Imagem principal', variations={'thumbnail': {'width': 590, 'height': 585 , 'crop': True}}, upload_to='sessao6',  blank=True)

    class Meta:
        verbose_name = 'SextaSessão'
        verbose_name_plural = 'SextaSessão'

        def __str__(self):
            return self.SextaSessão


class SetimaSessão(Base):
    subtituloSuperiorSetimaSessao = models.CharField('Subtitulo superior (sessão 7)', max_length=100, blank=True)
    tituloPrincipalSetimaSessao = models.CharField('Titulo principal', max_length=100, blank=True)
    primeiroTituloCardSetimaSessao = models.CharField('Titulo do primeiro card', max_length=100, blank=True)
    descrisaoPrimeiroCardSetimaSessao = models.CharField('Descrisao do primeiro card', max_length=200, blank=True)
    segundoTituloCardSetimaSessao = models.CharField('Titulo do segundo card', max_length=100, blank=True)
    descrisaoSegundoCardSetimaSessao = models.CharField('Descrisao do segundo card', max_length=200, blank=True)
    terceiroTituloCardSetimaSessao = models.CharField('Titulo do terceiro card', max_length=100, blank=True)
    descrisaoterceiroCardSetimaSessao = models.CharField('Descrisao do terceiro card', max_length=200, blank=True)


    class Meta:
        verbose_name = 'SetimaSessão'
        verbose_name_plural = 'SetimaSessão'

        def __str__(self):
            return self.SetimaSessão


class OitavaSessão(Base):
    subtituloSuperiorOitavaSessao = models.CharField('Subtitulo superior (sessão 8)', max_length=100, blank=True)
    tituloPrincipalOitavaSessao = models.CharField('Titulo principal', max_length=100, blank=True)
    descrisaoOitavaSessao = models.CharField('Descrisão principal', max_length=800, blank=True)
    botaoOitavaSessao = models.CharField('Botão', max_length=80, blank=True)
    imagemDoVideo = StdImageField('Imagem para o video', variations={'thumbnail': {'width': 780, 'height': 622 , 'crop': True}},upload_to='sessao8',  blank=True)

    class Meta:
        verbose_name = 'OitavaSessão'
        verbose_name_plural = 'OitavaSessão'

        def __str__(self):
            return self.OitavaSessão


class NonaSessão(Base):
    enderecoNonaSessao = models.CharField('Endereço (sessão 9)', max_length=800, blank=True)
    numeroNonaSessao = models.CharField('Numero de contato', max_length=100, blank=True)
    emailNonaSessao = models.CharField('Email', max_length=150, blank=True)
    logoInferior = StdImageField('Logo inferior', variations={'thumbnail': {'width': 166, 'height': 87, 'crop': True}},upload_to='logo',  blank=True)

    class Meta:
        verbose_name = 'NonaSessão'
        verbose_name_plural = 'NonaSessão'

        def __str__(self):
            return self.NonaSessão


class Rodapé(Base):
    copyrightRodape = models.CharField('Copyright rodapé', max_length=250, blank=True)
    nomeRodape = models.CharField('Nome de quem tem os direitos', max_length=100, blank=True)

    class Meta:
        verbose_name = 'Rodapé'
        verbose_name_plural = 'Rodapé'

        def __str__(self):
            return self.Rodapé