# Generated by Django 5.1.6 on 2025-03-11 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('calorias_por_grama', models.DecimalField(decimal_places=3, max_digits=6)),
                ('proteinas_por_grama', models.DecimalField(decimal_places=3, max_digits=6)),
                ('carboidratos_por_grama', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
        ),
    ]
