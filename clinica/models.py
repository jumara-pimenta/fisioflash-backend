from django.db import models

class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now=True, null=False)
    active = models.BooleanField(default=True, null=False)

    class Meta:
        managed = True
        abstract = True

class Paciente(ModelBase):
    class Gender(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMININO = 'F', 'Feminino'
        OUTRO = 'O', 'Outro'

    nome = models.CharField(db_column='nome', max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(db_column='data_nascimento', null=False)
    sexo = models.CharField(db_column='sexo', max_length=1, choices=Gender.choices, null=False)
    cpf = models.CharField(db_column='cpf', max_length=11, unique=True, null=False)
    rg = models.CharField(db_column='rg', max_length=10, unique=True, null=False)
    telefone = models.CharField(db_column='telefone', max_length=15, null=False)
    rua = models.CharField(db_column='rua', max_length=255, null=False)
    numero = models.CharField(db_column='numero', max_length=10, null=False)
    bairro = models.CharField(db_column='bairro', max_length=100, null=False)
    cep = models.CharField(db_column='cep', max_length=8, null=False)
    email = models.EmailField(db_column='email', unique=True, null=False)
    senha = models.CharField(db_column='senha', max_length=255, null=False)

    class Meta:
        db_table = 'paciente'

class Fisioterapeuta(ModelBase):
    class Gender(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMININO = 'F', 'Feminino'
        OUTRO = 'O', 'Outro'

    nome = models.CharField(db_column='nome', max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(db_column='data_nascimento', null=False)
    sexo = models.CharField(db_column='sexo', max_length=1, choices=Gender.choices, null=False)
    cpf = models.CharField(db_column='cpf', max_length=11, unique=True, null=False)
    rg = models.CharField(db_column='rg', max_length=10, unique=True, null=False)
    telefone = models.CharField(db_column='telefone', max_length=15, null=False)
    rua = models.CharField(db_column='rua', max_length=255, null=False)
    numero = models.CharField(db_column='numero', max_length=10, null=False)
    bairro = models.CharField(db_column='bairro', max_length=100, null=False)
    cep = models.CharField(db_column='cep', max_length=8, null=False)
    registro_profissional = models.CharField(db_column='registro_profissional', max_length=20, unique=True, null=False)
    especializacoes = models.TextField(db_column='especializacoes', null=False, blank=False)
    email = models.EmailField(db_column='email', unique=True, null=False)
    senha = models.CharField(db_column='senha', max_length=255, null=False)

    class Meta:
        db_table = 'fisioterapeuta'

class Servico(ModelBase):
    especialidade = models.CharField(db_column='especialidade', max_length=100, null=False, blank=False)

    class Meta:
        db_table = 'servico'


class CasoClinico(ModelBase):
    descricao = models.TextField(db_column='descricao', null=False, blank=False)
    paciente = models.ForeignKey('Paciente', on_delete=models.DO_NOTHING, db_column='paciente_id', related_name='casos_clinicos')
    fisioterapeuta = models.ForeignKey('Fisioterapeuta', on_delete=models.DO_NOTHING, db_column='fisioterapeuta_id', null=True, related_name='casos_clinicos')
    servico = models.ForeignKey('Servico', on_delete=models.DO_NOTHING, db_column='servico_id', null=True, related_name='casos_clinicos')

    class Meta:
        db_table = 'caso_clinico'
