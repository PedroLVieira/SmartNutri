# Generated by Django 5.1.6 on 2025-03-11 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('ingrediente', '0001_initial'),
        ('nutricionista', '0001_initial'),
        ('receita', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanoAlimentar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('observacoes', models.TextField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('ingredientes', models.ManyToManyField(to='ingrediente.ingrediente')),
                ('nutricionista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutricionista.nutricionista')),
                ('receitas', models.ManyToManyField(to='receita.receita')),
            ],
        ),
    ]
