from rest_framework import viewsets
from clinica import models, serializers
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [AllowAny]

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = models.Servico.objects.all()
    serializer_class = serializers.ServicoSerializer
    permission_classes = [IsAuthenticated]

class CasoClinicoViewSet(viewsets.ModelViewSet):
    queryset = models.CasoClinico.objects.all()
    serializer_class = serializers.CasoClinicoSerializer

class ServicoFisioterapeutaViewSet(viewsets.ModelViewSet):
    queryset = models.ServicoFisioterapeuta.objects.all()
    serializer_class = serializers.ServicoFisioterapeutaSerializer

    def get_queryset(self):
        servico_id = self.request.query_params.get('servico', None)
        if servico_id is not None:
            return ServicoFisioterapeuta.objects.filter(servico_id=servico_id)
        return super().get_queryset()  

class SolicitacaoAtendimentoViewSet(viewsets.ModelViewSet):
    queryset = models.SolicitacaoAtendimento.objects.all()
    serializer_class = serializers.SolicitacaoAtendimentoSerializer