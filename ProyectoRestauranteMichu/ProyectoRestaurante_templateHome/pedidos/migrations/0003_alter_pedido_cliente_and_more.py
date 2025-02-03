# Generated by Django 5.1.5 on 2025-02-01 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_alter_pedido_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='cliente',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre del Cliente'),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='nombre_cliente',
            field=models.CharField(max_length=100, null=True, verbose_name='Nombre del Cliente'),
        ),
    ]
