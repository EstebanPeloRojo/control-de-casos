# Generated by Django 5.0 on 2025-03-12 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudSoporte',
            fields=[
                ('ticket', models.AutoField(primary_key=True, serialize=False)),
                ('caso_usuario', models.CharField(max_length=200)),
                ('incidencia', models.CharField(max_length=255)),
                ('descripcion', models.TextField(max_length=255)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En proceso'), ('resuelto', 'Resuelto')], default='pendiente', max_length=20)),
            ],
        ),
    ]
