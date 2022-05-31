from django.db import models


# Create your models here.
class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificados = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class PaginaInicial(Base):
    tituloInicial = models.CharField('titulo (sessão 1)', max_length=100, blank=True)
    subTituloInicial = models.CharField('SubTítulo', max_length=100, blank=True)

    primeiraOpcao = models.CharField('1º (Barra de navegação)', max_length=100, blank=True)
    segundaOpcao = models.CharField('2º', max_length=100, blank=True)
    terceiraOpcao = models.CharField('3º', max_length=100, blank=True)
    quartaOpcao = models.CharField('4º', max_length=100, blank=True)
    quintaOpcao = models.CharField('5º', max_length=100, blank=True)
    sextaOpcao = models.CharField('6º', max_length=100, blank=True)
    ultimoBotao = models.CharField('7º', max_length=100, blank=True)

    pontosTitulo = models.CharField('Pontos titulo (sessão 2)', max_length=100, blank=True)
    primeiroPonto = models.CharField('Primeiro ponto', max_length=100, blank=True)
    terceiroPonto = models.CharField('Segundo ponto', max_length=100, blank=True)
    quintoPonto = models.CharField('Quinto ponto', max_length=100, blank=True)
    descrisaoPontos = models.CharField('Descrisão dos pontos', max_length=800, blank=True)

    primeiroTitulo = models.CharField('Primeiro titulo (sessão 3)', max_length=100, blank=True)
    primeiraDescrisao = models.CharField('Primeira descrisão', max_length=800, blank=True)
    primeiroBotao = models.CharField('Primeiro botão', max_length=80, blank=True)
    segundoTitulo = models.CharField('Segundo titulo (sessão 4)', max_length=100, blank=True)
    segundaDescrisao = models.CharField('Segunda descrisão', max_length=800, blank=True)
    primeiroTopico = models.CharField('Primeiro tópico', max_length=100, blank=True)
    segundoTopico = models.CharField('Segundo tópico', max_length=100, blank=True)
    terceiroTopico = models.CharField('Terceiro tópico', max_length=100, blank=True)
    segundoBotao = models.CharField('Segundo botão', max_length=80, blank=True)

    subtituloSuperior = models.CharField('Subtitulo superior (sessão 5)', max_length=100, blank=True)
    tituloQuintaSessao = models.CharField('Titulo', max_length=100, blank=True)
    descrisaoPrincipal = models.CharField('Descrisão principal', max_length=800, blank=True)
    botaoQuintaSessao = models.CharField('Botão principal', max_length=100, blank=True)
    primeiraDescrisaoIcone = models.CharField('Descrisão primeiro icone', max_length=250, blank=True)
    segundaDescrisaoIcone = models.CharField('Descrisão segundo icone', max_length=250, blank=True)
    terceiraDescrisaoIcone = models.CharField('Descrisão terceiro icone', max_length=250, blank=True)
    quartaDescrisaoIcone = models.CharField('Descrisão quarto icone', max_length=250, blank=True)
    quintaDescrisaoIcone = models.CharField('Descrisão quinto icone', max_length=250, blank=True)

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

    subtituloSuperiorSetimaSessao = models.CharField('Subtitulo superior (sessão 7)', max_length=100, blank=True)
    tituloPrincipalSetimaSessao = models.CharField('Titulo principal', max_length=100, blank=True)
    primeiroTituloCardSetimaSessao = models.CharField('Titulo do primeiro card', max_length=100, blank=True)
    descrisaoPrimeiroCardSetimaSessao = models.CharField('Descrisao do primeiro card', max_length=200, blank=True)
    segundoTituloCardSetimaSessao = models.CharField('Titulo do segundo card', max_length=100, blank=True)
    descrisaoSegundoCardSetimaSessao = models.CharField('Descrisao do segundo card', max_length=200, blank=True)
    terceiroTituloCardSetimaSessao = models.CharField('Titulo do terceiro card', max_length=100, blank=True)
    descrisaoterceiroCardSetimaSessao = models.CharField('Descrisao do terceiro card', max_length=200, blank=True)

    subtituloSuperiorOitavaSessao = models.CharField('Subtitulo superior (sessão 8)', max_length=100, blank=True)
    tituloPrincipalOitavaSessao = models.CharField('Titulo principal', max_length=100, blank=True)
    descrisaoOitavaSessao = models.CharField('Descrisão principal', max_length=800, blank=True)
    botaoOitavaSessao = models.CharField('Botão', max_length=80, blank=True)

    enderecoNonaSessao = models.CharField('Endereço (sessão 9)', max_length=800, blank=True)
    numeroNonaSessao = models.CharField('Numero de contato', max_length=100, blank=True)
    emailNonaSessao = models.CharField('Email', max_length=150, blank=True)

    copyrightRodape = models.CharField('Copyright rodapé', max_length=250, blank=True)
    nomeRodape = models.CharField('Nome de quem tem os direitos', max_length=100, blank=True)

    class Meta:
        verbose_name = 'Pagina Inicial'
        verbose_name_plural = 'Paginas Iniciais'

        def __str__(self):
            return self.tituloInicial
