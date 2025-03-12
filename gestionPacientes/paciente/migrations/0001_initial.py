# Generated by Django 3.2.6 on 2025-03-12 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sistemaHospitalario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('genero', models.CharField(max_length=50)),
                ('contactoEmergencia', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('sistemaHospitalario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistemaHospitalario.sistemahospitalario')),
            ],
        ),
    ]
