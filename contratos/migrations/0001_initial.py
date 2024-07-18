# Generated by Django 4.1.2 on 2024-04-23 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razón_social', models.CharField(default='DIGITAL BRIDGE COMMUNICATIONS', max_length=255)),
                ('nit_empresa', models.CharField(default='9014814305', max_length=20)),
                ('nombre_representante_legal', models.CharField(default='Jonathan Cifuentes Cadena', max_length=255)),
                ('cargo_representante_legal', models.CharField(default='Gerente', max_length=255)),
                ('tipo_doc_representante_legal', models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('P', 'Pasaporte')], default='CC', max_length=255)),
                ('numero_doc_representante_legal', models.CharField(default='1016019519', max_length=20)),
                ('lugar_expedicion_doc_representante_legal', models.CharField(default='Bogotá', max_length=255)),
                ('celular_representante_legal', models.CharField(default='+1 (336) 899-7553', max_length=20)),
                ('correo_representante_legal', models.EmailField(default='jcifuentes@dbcw.com.co', max_length=255)),
                ('ubicacion', models.CharField(default='Jenesano-Boyacá', max_length=255)),
                ('direccion_notificacion_judicial', models.CharField(default='Cl. #8-42', max_length=255)),
                ('cargo_contrato', models.CharField(max_length=255)),
                ('tipo_contrato', models.CharField(choices=[('Contrato de Trabajo a Tiempo Completo - Término Fijo', 'Contrato de Trabajo a Tiempo Completo - Término Fijo'), ('Contrato de Trabajo a Tiempo Parcial - Término Fijo', 'Contrato de Trabajo a Tiempo Parcial - Término Fijo'), ('Contrato de Aprendizaje', 'Contrato de Aprendizaje')], max_length=255)),
                ('salario', models.DecimalField(decimal_places=0, max_digits=10)),
                ('duracion_contrato', models.CharField(max_length=255)),
                ('fecha_inicio', models.DateField()),
                ('fecha_terminacion', models.DateField()),
                ('fecha_pre_aviso', models.DateField()),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Terminado', 'Terminado')], default='Activo', max_length=100)),
                ('fecha_creacion_contrato', models.DateField(auto_now_add=True)),
                ('adjunto_contrato', models.FileField(upload_to='adjuntos_contratos/')),
                ('fecha_carga_adjunto_contrato', models.DateField(auto_now_add=True)),
                ('adjunto_preaviso', models.FileField(upload_to='adjuntos_preaviso/')),
                ('fecha_carga_adjunto_preaviso', models.DateField(auto_now_add=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.persona')),
            ],
        ),
    ]