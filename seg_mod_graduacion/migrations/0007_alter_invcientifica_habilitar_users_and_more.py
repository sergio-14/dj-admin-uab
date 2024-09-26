# Generated by Django 5.1 on 2024-09-24 15:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seg_mod_graduacion', '0006_alter_logica_options_invcientifica_habilitar_users_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='invcientifica',
            name='habilitar_users',
            field=models.BooleanField(default=False, verbose_name='¡Si el proyecto consta mas de un participante click aqui!'),
        ),
        migrations.AlterField(
            model_name='invcientifica',
            name='user_dos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='name_userdos', to=settings.AUTH_USER_MODEL, verbose_name='Tercer participante'),
        ),
        migrations.AlterField(
            model_name='invcientifica',
            name='user_uno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='name_useruno', to=settings.AUTH_USER_MODEL, verbose_name='Segundo participante'),
        ),
    ]
