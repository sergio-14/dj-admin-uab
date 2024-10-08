# Generated by Django 5.1 on 2024-08-30 15:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HabilitarFechas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio_habilitacion', models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio de Habilitación')),
                ('fecha_fin_habilitacion', models.DateField(blank=True, null=True, verbose_name='Fecha Fin de Habilitación')),
            ],
            options={
                'verbose_name': 'Habilitar Fecha',
                'verbose_name_plural': 'Habilitacion de Fechas',
            },
        ),
        migrations.CreateModel(
            name='T_Fase',
            fields=[
                ('Id_fase', models.AutoField(primary_key=True, serialize=False)),
                ('S_Fase', models.CharField(max_length=100, verbose_name='Fase o Etapa del Proyecto')),
            ],
            options={
                'verbose_name': 'Fase Proyecto',
                'verbose_name_plural': 'Fases del Proyecto ',
            },
        ),
        migrations.CreateModel(
            name='T_Gestion',
            fields=[
                ('Id_Ges', models.AutoField(primary_key=True, serialize=False)),
                ('S_Gestion', models.CharField(max_length=100, verbose_name='Gestion y periodo')),
            ],
            options={
                'verbose_name': 'Periodo Gestion',
                'verbose_name_plural': 'Periodo y Gestion',
            },
        ),
        migrations.CreateModel(
            name='T_Semestre',
            fields=[
                ('Id_Semestre', models.AutoField(primary_key=True, serialize=False)),
                ('S_Semestre', models.CharField(max_length=100, verbose_name='Semestre')),
            ],
            options={
                'verbose_name': 'Semestre',
                'verbose_name_plural': 'Semestres',
            },
        ),
        migrations.CreateModel(
            name='T_Tipo',
            fields=[
                ('Id_tipo', models.AutoField(primary_key=True, serialize=False)),
                ('S_Tipo', models.CharField(max_length=100, verbose_name='Tipo de Investigación Social.')),
            ],
            options={
                'verbose_name': 'Tipo Proyecto',
                'verbose_name_plural': 'Tipo de Proyectos ',
            },
        ),
        migrations.CreateModel(
            name='T_Materia',
            fields=[
                ('Id_Materia', models.AutoField(primary_key=True, serialize=False)),
                ('S_Materia', models.CharField(max_length=100, verbose_name='Materia')),
                ('T_Semestre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interaccion_social.t_semestre', verbose_name='Semestre')),
            ],
            options={
                'verbose_name': 'Materia',
                'verbose_name_plural': 'Materias',
            },
        ),
        migrations.CreateModel(
            name='T_Proyectos_IIISP',
            fields=[
                ('Id_Proyect', models.AutoField(primary_key=True, serialize=False)),
                ('S_Titulo', models.CharField(max_length=150, verbose_name='Titulo')),
                ('Fecha_Inicio', models.DateField()),
                ('Fecha_Finalizacion', models.DateField()),
                ('S_Descripcion', models.TextField(blank=True, verbose_name='Descripcion')),
                ('S_Documentacion', models.FileField(null=True, upload_to='Documento/', verbose_name='Documentacion')),
                ('S_Imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
                ('S_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario relacionado')),
                ('T_Fase_proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interaccion_social.t_fase', verbose_name='Fase del Proyecto')),
                ('T_Gestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interaccion_social.t_gestion', verbose_name='Gestion')),
                ('T_Materia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='interaccion_social.t_materia', verbose_name='Materia')),
                ('T_Tipo_Proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interaccion_social.t_tipo', verbose_name='Tipo de Proyecto')),
            ],
            options={
                'verbose_name': 'Trabajos IIISP',
                'verbose_name_plural': 'Proyectos IIISP',
            },
        ),
    ]
