# Generated by Django 5.0 on 2025-06-02 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casos', '0002_feedbacktecnico'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbacktecnico',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='HistorialEstado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=20)),
                ('fecha_cambio', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.TextField(blank=True, max_length=255, null=True)),
                ('solicitud_soporte', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='historial_estado', to='casos.solicitudsoporte')),
            ],
            options={
                'verbose_name': 'Historial de Estado',
                'verbose_name_plural': 'Historial de Estados',
            },
        ),
    ]
