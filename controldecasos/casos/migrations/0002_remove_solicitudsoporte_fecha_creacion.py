# Generated by Django 4.2 on 2025-02-14 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitudsoporte',
            name='fecha_creacion',
        ),
    ]
