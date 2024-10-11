from rest_framework import viewsets
from clinica import models, serializers
from rest_framework.permissions import AllowAny

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [AllowAny]

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = models.Servico.objects.all()
    serializer_class = serializers.ServicoSerializer

class CasoClinicoViewSet(viewsets.ModelViewSet):
    queryset = models.CasoClinico.objects.all()
    serializer_class = serializers.CasoClinicoSerializer