# Generated by Django 4.1.2 on 2024-04-23 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cargo', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
            ],
        ),
    ]