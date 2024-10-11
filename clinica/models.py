import re
from django.db import models
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Custom User Manager
class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(
            username=username, email=email, is_staff=is_staff,
            is_active=True, is_superuser=is_superuser, last_login=now,
            date_joined=now, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


# Custom User Model
class User(AbstractBaseUser, PermissionsMixin):
    class UserType(models.TextChoices):
        PACIENTE = 'PAC', _('Paciente')
        FISIOTERAPEUTA = 'FIS', _('Fisioterapeuta')

    username = models.CharField(
        _('username'), max_length=15, unique=True,
        help_text=_('Required. 15 characters or fewer. Letters, numbers and @/./+/-/_ characters'),
        validators=[
            validators.RegexValidator(
                re.compile(r'^[\w.@+-]+$'), _('Enter a valid username.'), _('invalid')
            )
        ]
    )
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    is_staff = models.BooleanField(
        _('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.')
    )
    is_active = models.BooleanField(
        _('active'), default=True,
        help_text=_(
            'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    user_type = models.CharField(
        _('User Type'), max_length=3, choices=UserType.choices, default=UserType.PACIENTE
    )

    cpf = models.CharField(db_column='cpf', max_length=11, unique=True, null=False)
    rg = models.CharField(db_column='rg', max_length=10, unique=True, null=False)
    telefone = models.CharField(db_column='telefone', max_length=15, null=False)
    rua = models.CharField(db_column='rua', max_length=255, null=False)
    numero = models.CharField(db_column='numero', max_length=10, null=False)
    bairro = models.CharField(db_column='bairro', max_length=100, null=False)
    cep = models.CharField(db_column='cep', max_length=8, null=False)
    data_nascimento = models.DateField(db_column='data_nascimento', null=True)

    registro_profissional = models.CharField(db_column='registro_profissional', max_length=20, unique=True, null=True,
                                             blank=True)
    especializacoes = models.TextField(db_column='especializacoes', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    class Meta:
        managed = True
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])


# Modelo de Serviços
class Servico(models.Model):
    especialidade = models.CharField(db_column='especialidade', max_length=100, null=False, blank=False)

    class Meta:
        db_table = 'servico'


# Modelo intermediário para relacionar Fisioterapeuta e Serviço
class ServicoFisioterapeuta(models.Model):
    fisioterapeuta = models.ForeignKey('User', on_delete=models.DO_NOTHING, db_column='fisioterapeuta_id',
                                       limit_choices_to={'user_type': 'FIS'})
    servico = models.ForeignKey('Servico', on_delete=models.CASCADE, db_column='servico_id')

    class Meta:
        db_table = 'servico_fisioterapeuta'



# Modelo de Caso Clínico
class CasoClinico(models.Model):
    descricao = models.TextField(db_column='descricao', null=False, blank=False)

    # Relacionamento com Paciente
    paciente = models.ForeignKey('User', on_delete=models.DO_NOTHING, db_column='paciente_id',
                                 limit_choices_to={'user_type': 'PAC'})

    # Relacionamento com Serviço/Fisioterapeuta
    servico_fisioterapeuta = models.ForeignKey('ServicoFisioterapeuta', on_delete=models.DO_NOTHING,
                                               db_column='servico_fisioterapeuta_id', null=True)

    # Situação do caso clínico
    SITUACAO_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em tratamento', 'Em tratamento'),
        ('Concluído', 'Concluído'),
        ('Recusado', 'Recusado')
    ]
    situacao = models.CharField(db_column='situacao', max_length=20, choices=SITUACAO_CHOICES, default='Pendente')

    class Meta:
        db_table = 'caso_clinico'
