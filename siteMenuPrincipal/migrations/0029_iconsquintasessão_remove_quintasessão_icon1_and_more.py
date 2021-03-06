# Generated by Django 4.0.4 on 2022-06-28 11:45

import ckeditor_uploader.fields
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('siteMenuPrincipal', '0028_alter_barradenavegação_logonav_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='iconsQuintaSessão',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificados', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('icon1', stdimage.models.StdImageField(blank=True, upload_to='icons', verbose_name='Primeiro icone')),
                ('primeiraDescrisaoIcone', models.CharField(blank=True, max_length=250, verbose_name='Descrisão primeiro icone')),
                ('icon2', stdimage.models.StdImageField(blank=True, upload_to='icons', verbose_name='Segundo icone')),
                ('segundaDescrisaoIcone', models.CharField(blank=True, max_length=250, verbose_name='Descrisão segundo icone')),
                ('icon3', stdimage.models.StdImageField(blank=True, upload_to='icons', verbose_name='Terceiro icone')),
                ('terceiraDescrisaoIcone', models.CharField(blank=True, max_length=250, verbose_name='Descrisão terceiro icone')),
                ('icon4', stdimage.models.StdImageField(blank=True, upload_to='icons', verbose_name='Quarto icone')),
                ('quartaDescrisaoIcone', models.CharField(blank=True, max_length=250, verbose_name='Descrisão quarto icone')),
                ('icon5', stdimage.models.StdImageField(blank=True, upload_to='icons', verbose_name='Quinto icone')),
                ('quintaDescrisaoIcone', models.CharField(blank=True, max_length=250, verbose_name='Descrisão quinto icone')),
                ('imagemDireita', stdimage.models.StdImageField(blank=True, upload_to='sessao5', verbose_name='Imagem na direita')),
            ],
            options={
                'verbose_name': 'iconsQuintaSessão',
                'verbose_name_plural': 'iconsQuintaSessão',
            },
        ),
        migrations.RemoveField(
            model_name='quintasessão',
            name='icon1',
        ),
        migrations.RemoveField(
            model_name='quintasessão',
            name='icon2',
        ),
        migrations.RemoveField(
            model_name='quintasessão',
            name='icon3',
        ),
        migrations.RemoveField(
            model_name='quintasessão',
            name='icon4',
        ),
        migrations.RemoveField(
            model_name='quintasessão',
            name='icon5',
        ),
        migrations.RemoveField(
            model_name='quintasessão',
            name='imagemDireita',
        ),
        migrations.RemoveField(
            model_name='quintasessão',
            name='primeiraDescrisaoIcone',
        ),
        migrations.RemoveField(
            model_name='quintasessão',
            name='quartaDescrisaoIcone',
        ),
        migrations.RemoveField(
            model_name='quintasessão',
            name='quintaDescrisaoIcone',
        ),
        migrations.RemoveField(
            model_name='quintasessão',
            name='segundaDescrisaoIcone',
        ),
        migrations.RemoveField(
            model_name='quintasessão',
            name='terceiraDescrisaoIcone',
        ),
        migrations.AlterField(
            model_name='quintasessão',
            name='descrisaoPrincipal',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=800, verbose_name='Descrisão principal'),
        ),
    ]
