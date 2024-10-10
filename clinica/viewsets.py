from rest_framework import viewsets
from clinica import models, serializers

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = models.Paciente.objects.all()
    serializer_class = serializers.PacienteSerializer


class FisioterapeutaViewSet(viewsets.ModelViewSet):
    queryset = models.Fisioterapeuta.objects.all()
    serializer_class = serializers.FisioterapeutaSerializer


class ServicoViewSet(viewsets.ModelViewSet):
    queryset = models.Servico.objects.all()
    serializer_class = serializers.ServicoSerializer


class CasoClinicoViewSet(viewsets.ModelViewSet):
    queryset = models.CasoClinico.objects.all()
    serializer_class = serializers.CasoClinicoSerializer