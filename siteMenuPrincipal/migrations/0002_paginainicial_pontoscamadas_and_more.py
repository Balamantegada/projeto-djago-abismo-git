# Generated by Django 4.0.4 on 2022-05-26 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteMenuPrincipal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paginainicial',
            name='pontosCamadas',
            field=models.CharField(blank=True, max_length=100, verbose_name='Pontos Camadas'),
        ),
        migrations.AlterField(
            model_name='paginainicial',
            name='tituloInicial',
            field=models.CharField(blank=True, max_length=100, verbose_name='titulo'),
        ),
    ]
