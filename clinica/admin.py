from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import User, Servico, CasoClinico, ServicoFisioterapeuta

# Registra o modelo de Usuário
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_active', 'user_type')
    search_fields = ('email', 'username', 'first_name', 'last_name')

# Registra o modelo de Serviço
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('especialidade',)
    search_fields = ('especialidade',)

# Registra o modelo de Caso Clínico
@admin.register(CasoClinico)
class CasoClinicoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'paciente', 'servico_fisioterapeuta', 'situacao')
    search_fields = ('descricao',)

# Registra o modelo de Fisioterapeuta_Servico
@admin.register(ServicoFisioterapeuta)
class ServicoFisioterapeutaAdmin(admin.ModelAdmin):
    list_display = ('fisioterapeuta', 'servico')
    search_fields = ('fisioterapeuta', 'servico')

