# Generated by Django 4.2.3 on 2023-07-14 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_veiculo_serviço'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='serviço',
        ),
    ]
