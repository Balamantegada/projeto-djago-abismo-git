# Generated by Django 4.0.4 on 2022-05-26 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteMenuPrincipal', '0016_paginainicial_emailnonasessao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paginainicial',
            name='copyrightRodape',
            field=models.CharField(blank=True, max_length=250, verbose_name='Copyright rodapé'),
        ),
        migrations.AddField(
            model_name='paginainicial',
            name='nomeRodape',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nome de quem tem os direitos'),
        ),
    ]
