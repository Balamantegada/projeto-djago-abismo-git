# Generated by Django 4.0.4 on 2022-05-26 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteMenuPrincipal', '0009_paginainicial_primeirobotao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paginainicial',
            name='primeiroTopico',
            field=models.CharField(blank=True, max_length=100, verbose_name='Primeiro tópico'),
        ),
        migrations.AddField(
            model_name='paginainicial',
            name='segundoTopico',
            field=models.CharField(blank=True, max_length=100, verbose_name='Segundo tópico'),
        ),
        migrations.AddField(
            model_name='paginainicial',
            name='terceiroTopico',
            field=models.CharField(blank=True, max_length=100, verbose_name='Terceiro tópico'),
        ),
        migrations.AlterField(
            model_name='paginainicial',
            name='segundoTitulo',
            field=models.CharField(blank=True, max_length=100, verbose_name='Segundo titulo sessão 4'),
        ),
    ]
