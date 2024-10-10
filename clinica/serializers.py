from rest_framework import serializers
from clinica import models

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paciente
        fields = '__all__'

class FisioterapeutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fisioterapeuta
        fields = '__all__'

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Servico
        fields = '__all__'


class CasoClinicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CasoClinico
        fields = '__all__'