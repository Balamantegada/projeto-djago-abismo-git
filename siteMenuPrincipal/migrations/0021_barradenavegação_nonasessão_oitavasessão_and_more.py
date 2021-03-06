# Generated by Django 4.0.4 on 2022-06-07 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteMenuPrincipal', '0020_alter_paginainicial_primeiraopcao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarradeNavegação',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificados', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('primeiraOpcao', models.CharField(blank=True, max_length=100, verbose_name='1º (Barra de navegação)')),
                ('segundaOpcao', models.CharField(blank=True, max_length=100, verbose_name='2º')),
                ('terceiraOpcao', models.CharField(blank=True, max_length=100, verbose_name='3º')),
                ('quartaOpcao', models.CharField(blank=True, max_length=100, verbose_name='4º')),
                ('quintaOpcao', models.CharField(blank=True, max_length=100, verbose_name='5º')),
                ('sextaOpcao', models.CharField(blank=True, max_length=100, verbose_name='6º')),
                ('ultimoBotao', models.CharField(blank=True, max_length=100, verbose_name='7º')),
            ],
            options={
                'verbose_name': 'BarradeNavegação',
                'verbose_name_plural': 'BarrasdeNavegações',
            },
        ),
        migrations.CreateModel(
            name='NonaSessão',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificados', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('enderecoNonaSessao', models.CharField(blank=True, max_length=800, verbose_name='Endereço (sessão 9)')),
                ('numeroNonaSessao', models.CharField(blank=True, max_length=100, verbose_name='Numero de contato')),
                ('emailNonaSessao', models.CharField(blank=True, max_length=150, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'NonaSessão',
                'verbose_name_plural': 'NonaSessão',
            },
        ),
        migrations.CreateModel(
            name='OitavaSessão',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificados', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('subtituloSuperiorOitavaSessao', models.CharField(blank=True, max_length=100, verbose_name='Subtitulo superior (sessão 8)')),
                ('tituloPrincipalOitavaSessao', models.CharField(blank=True, max_length=100, verbose_name='Titulo principal')),
                ('descrisaoOitavaSessao', models.CharField(blank=True, max_length=800, verbose_name='Descrisão principal')),
                ('botaoOitavaSessao', models.CharField(blank=True, max_length=80, verbose_name='Botão')),
            ],
            options={
                'verbose_name': 'OitavaSessão',
                'verbose_name_plural': 'OitavaSessão',
            },
        ),
        migrations.CreateModel(
            name='ParteInicial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificados', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('tituloInicial', models.CharField(blank=True, max_length=100, verbose_name='titulo (sessão 1)')),
                ('subTituloInicial', models.CharField(blank=True, max_length=100, verbose_name='SubTítulo')),
            ],
            options={
                'verbose_name': 'ParteInicial',
                'verbose_name_plural': 'PartesIniciais',
            },
        ),
        migrations.CreateModel(
            name='QuartaSessão',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificados', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('segundoTitulo', models.CharField(blank=True, max_length=100, verbose_name='Segundo titulo (sessão 4)')),
                ('segundaDescrisao', models.CharField(blank=True, max_length=800, verbose_name='Segunda descrisão')),
                ('primeiroTopico', models.CharField(blank=True, max_length=100, verbose_name='Primeiro tópico')),
                ('segundoTopico', models.CharField(blank=True, max_length=100, verbose_name='Segundo tópico')),
                ('terceiroTopico', models.CharField(blank=True, max_length=100, verbose_name='Terceiro tópico')),
                ('segundoBotao', models.CharField(blank=True, max_length=80, verbose_name='Segundo botão')),
            ],
            options={
                'verbose_name': 'QuartaSessão',
                'verbose_name_plural': 'QuartaSessão',
            },
        ),
        migrations.CreateModel(
            name='QuintaSessão',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificados', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('subtituloSuperior', models.CharField(blank=True, max_length=100, verbose_name='Subtitulo superior (sessão 5)')),
                ('tituloQuintaSessao', models.CharField(blank=True, max_length=100, verbose_name='Titulo')),
                ('descrisaoPrincipal', models.CharField(blank=True, max_length=800, verbose_name='Descrisão principal')),
                ('botaoQuintaSessao', models.CharField(blank=True, max_length=100, verbose_name='Botão principal')),
                ('primeiraDescrisaoIcone', models.CharField(blank=True, max_length=250, verbose_name='Descrisão primeiro icone')),
                ('segundaDescrisaoIcone', models.CharField(blank=True, max_length=250, verbose_name='Descrisão segundo icone')),
                ('terceiraDescrisaoIcone', models.CharField(blank=True, max_length=250, verbose_name='Descrisão terceiro icone')),
                ('quartaDescrisaoIcone', models.CharField(blank=True, max_length=250, verbose_name='Descrisão quarto icone')),
                ('quintaDescrisaoIcone', models.CharField(blank=True, max_length=250, verbose_name='Descrisão quinto icone')),
            ],
            options={
                'verbose_name': 'QuintaSessão',
                'verbose_name_plural': 'QuintaSessão',
            },
        ),
        migrations.CreateModel(
            name='Rodapé',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificados', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('copyrightRodape', models.CharField(blank=True, max_length=250, verbose_name='Copyright rodapé')),
                ('nomeRodape', models.CharField(blank=True, max_length=100, verbose_name='Nome de quem tem os direitos')),
            ],
            options={
                'verbose_name': 'Rodapé',
                'verbose_name_plural': 'Rodapé',
            },
        ),
        migrations.CreateModel(
            name='SegundaSessão',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificados', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('pontosTitulo', models.CharField(blank=True, max_length=100, verbose_name='Pontos titulo (sessão 2)')),
                ('primeiroPonto', models.CharField(blank=True, max_length=100, verbose_name='Primeiro ponto')),
                ('terceiroPonto', models.CharField(blank=True, max_length=100, verbose_name='Segundo ponto')),
                ('quintoPonto', models.CharField(blank=True, max_length=100, verbose_name='Quinto ponto')),
                ('descrisaoPontos', models.CharField(blank=True, max_length=800, verbose_name='Descrisão dos pontos')),
            ],
            options={
                'verbose_name': 'SegundaSessão',
                'verbose_name_plural': 'SegundaSessão',
            },
        ),
        migrations.CreateModel(
            name='SetimaSessão',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificados', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('subtituloSuperiorSetimaSessao', models.CharField(blank=True, max_length=100, verbose_name='Subtitulo superior (sessão 7)')),
                ('tituloPrincipalSetimaSessao', models.CharField(blank=True, max_length=100, verbose_name='Titulo principal')),
                ('primeiroTituloCardSetimaSessao', models.CharField(blank=True, max_length=100, verbose_name='Titulo do primeiro card')),
                ('descrisaoPrimeiroCardSetimaSessao', models.CharField(blank=True, max_length=200, verbose_name='Descrisao do primeiro card')),
                ('segundoTituloCardSetimaSessao', models.CharField(blank=True, max_length=100, verbose_name='Titulo do segundo card')),
                ('descrisaoSegundoCardSetimaSessao', models.CharField(blank=True, max_length=200, verbose_name='Descrisao do segundo card')),
                ('terceiroTituloCardSetimaSessao', models.CharField(blank=True, max_length=100, verbose_name='Titulo do terceiro card')),
                ('descrisaoterceiroCardSetimaSessao', models.CharField(blank=True, max_length=200, verbose_name='Descrisao do terceiro card')),
            ],
            options={
                'verbose_name': 'SetimaSessão',
                'verbose_name_plural': 'SetimaSessão',
            },
        ),
        migrations.CreateModel(
            name='SextaSessão',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificados', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('tituloPrincipalSextaSessao', models.CharField(blank=True, max_length=100, verbose_name='Titulo principal (sesssão 6)')),
                ('primeiroSubtituloSextaSessao', models.CharField(blank=True, max_length=100, verbose_name='Primeiro subtitulo')),
                ('primeiraDescrisaoSextaSesssao', models.CharField(blank=True, max_length=400, verbose_name='Primeira descrisão')),
                ('segundoSubtituloSextaSessao', models.CharField(blank=True, max_length=100, verbose_name='Segundo subtitulo')),
                ('segundaDescrisaoSextaSesssao', models.CharField(blank=True, max_length=400, verbose_name='Segunda descrisão')),
                ('terceiroSubtituloSextaSessao', models.CharField(blank=True, max_length=100, verbose_name='Terceiro subtitulo')),
                ('terceiraDescrisaoSextaSesssao', models.CharField(blank=True, max_length=400, verbose_name='Terceira descrisão')),
                ('quartoSubtituloSextaSessao', models.CharField(blank=True, max_length=100, verbose_name='Quarto subtitulo')),
                ('quartaDescrisaoSextaSesssao', models.CharField(blank=True, max_length=400, verbose_name='Quarta descrisão')),
                ('botaoSextaSessao', models.CharField(blank=True, max_length=80, verbose_name='Botão')),
            ],
            options={
                'verbose_name': 'SextaSessão',
                'verbose_name_plural': 'SextaSessão',
            },
        ),
        migrations.CreateModel(
            name='TerceiraSessão',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificados', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('primeiroTitulo', models.CharField(blank=True, max_length=100, verbose_name='Primeiro titulo (sessão 3)')),
                ('primeiraDescrisao', models.CharField(blank=True, max_length=800, verbose_name='Primeira descrisão')),
                ('primeiroBotao', models.CharField(blank=True, max_length=80, verbose_name='Primeiro botão')),
            ],
            options={
                'verbose_name': 'TerceiraSessão',
                'verbose_name_plural': 'TerceiraSessão',
            },
        ),
        migrations.DeleteModel(
            name='PaginaInicial',
        ),
    ]
