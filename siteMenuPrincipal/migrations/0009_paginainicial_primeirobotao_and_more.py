# Generated by Django 4.0.4 on 2022-05-26 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteMenuPrincipal', '0008_remove_paginainicial_pontoscamadastitulo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paginainicial',
            name='primeiroBotao',
            field=models.CharField(blank=True, max_length=80, verbose_name='Primeiro botão'),
        ),
        migrations.AddField(
            model_name='paginainicial',
            name='segundoBotao',
            field=models.CharField(blank=True, max_length=80, verbose_name='Segundo botão'),
        ),
    ]
