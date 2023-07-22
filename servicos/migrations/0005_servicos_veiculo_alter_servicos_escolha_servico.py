# Generated by Django 4.2.3 on 2023-07-14 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_alter_veiculo_veiculo'),
        ('servicos', '0004_remove_servicos_veiculos_serv_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicos',
            name='veiculo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clientes.veiculo'),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='escolha_servico',
            field=models.CharField(choices=[('LC', 'lavagem_completa'), ('ML', 'meia_lavagem')], db_column='escolha_servico', default='ML', max_length=2),
        ),
    ]