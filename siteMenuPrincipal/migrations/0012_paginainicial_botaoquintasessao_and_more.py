# Generated by Django 4.0.4 on 2022-05-26 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteMenuPrincipal', '0011_paginainicial_descrisaoprincipal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paginainicial',
            name='botaoQuintaSessao',
            field=models.CharField(blank=True, max_length=100, verbose_name='Botão principal'),
        ),
        migrations.AddField(
            model_name='paginainicial',
            name='primeiraDescrisaoIcone',
            field=models.CharField(blank=True, max_length=250, verbose_name='Descrisão primeiro icone'),
        ),
        migrations.AddField(
            model_name='paginainicial',
            name='quartaDescrisaoIcone',
            field=models.CharField(blank=True, max_length=250, verbose_name='Descrisão quarto icone'),
        ),
        migrations.AddField(
            model_name='paginainicial',
            name='quintaDescrisaoIcone',
            field=models.CharField(blank=True, max_length=250, verbose_name='Descrisão quinto icone'),
        ),
        migrations.AddField(
            model_name='paginainicial',
            name='segundaDescrisaoIcone',
            field=models.CharField(blank=True, max_length=250, verbose_name='Descrisão segundo icone'),
        ),
        migrations.AddField(
            model_name='paginainicial',
            name='terceiraDescrisaoIcone',
            field=models.CharField(blank=True, max_length=250, verbose_name='Descrisão terceiro icone'),
        ),
    ]
