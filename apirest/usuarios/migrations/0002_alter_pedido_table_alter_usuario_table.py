# Generated by Django 5.1.6 on 2025-02-15 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='pedido',
            table='pedidos',
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='usuarios',
        ),
    ]
