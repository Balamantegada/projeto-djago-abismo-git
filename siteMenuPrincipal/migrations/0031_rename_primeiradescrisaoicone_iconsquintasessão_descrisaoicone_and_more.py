# Generated by Django 4.0.4 on 2022-06-28 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteMenuPrincipal', '0030_remove_iconsquintasessão_imagemdireita_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iconsquintasessão',
            old_name='primeiraDescrisaoIcone',
            new_name='DescrisaoIcone',
        ),
        migrations.RenameField(
            model_name='iconsquintasessão',
            old_name='icon1',
            new_name='icon',
        ),
        migrations.RemoveField(
            model_name='iconsquintasessão',
            name='icon2',
        ),
        migrations.RemoveField(
            model_name='iconsquintasessão',
            name='icon3',
        ),
        migrations.RemoveField(
            model_name='iconsquintasessão',
            name='icon4',
        ),
        migrations.RemoveField(
            model_name='iconsquintasessão',
            name='icon5',
        ),
        migrations.RemoveField(
            model_name='iconsquintasessão',
            name='quartaDescrisaoIcone',
        ),
        migrations.RemoveField(
            model_name='iconsquintasessão',
            name='quintaDescrisaoIcone',
        ),
        migrations.RemoveField(
            model_name='iconsquintasessão',
            name='segundaDescrisaoIcone',
        ),
        migrations.RemoveField(
            model_name='iconsquintasessão',
            name='terceiraDescrisaoIcone',
        ),
    ]
