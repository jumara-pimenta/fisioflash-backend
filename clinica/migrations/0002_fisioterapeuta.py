# Generated by Django 5.1.2 on 2024-10-09 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fisioterapeuta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('nome', models.CharField(db_column='nome', max_length=100)),
                ('data_nascimento', models.DateField(db_column='data_nascimento')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], db_column='sexo', max_length=1)),
                ('cpf', models.CharField(db_column='cpf', max_length=11, unique=True)),
                ('rg', models.CharField(db_column='rg', max_length=10, unique=True)),
                ('telefone', models.CharField(db_column='telefone', max_length=15)),
                ('rua', models.CharField(db_column='rua', max_length=255)),
                ('numero', models.CharField(db_column='numero', max_length=10)),
                ('bairro', models.CharField(db_column='bairro', max_length=100)),
                ('cep', models.CharField(db_column='cep', max_length=8)),
                ('registro_profissional', models.CharField(db_column='registro_profissional', max_length=20, unique=True)),
                ('especializacoes', models.TextField(db_column='especializacoes')),
                ('email', models.EmailField(db_column='email', max_length=254, unique=True)),
                ('senha', models.CharField(db_column='senha', max_length=255)),
            ],
            options={
                'db_table': 'fisioterapeuta',
            },
        ),
    ]
