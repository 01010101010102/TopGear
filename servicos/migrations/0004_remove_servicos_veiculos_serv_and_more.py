# Generated by Django 4.2.3 on 2023-07-14 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_veiculo_serviço'),
        ('servicos', '0003_remove_servicos_veiculos_servicos_veiculos_serv_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicos',
            name='veiculos_serv',
        ),
        migrations.AlterField(
            model_name='servicos',
            name='escolha_servico',
            field=models.OneToOneField(choices=[('LC', 'lavagem_completa'), ('ML', 'meia_lavagem')], db_column='escolha_servico', max_length=2, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.veiculo'),
        ),
    ]
