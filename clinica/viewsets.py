from rest_framework import viewsets
from clinica import models, serializers
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

    def perform_create(self, serializer):
        caso_clinico = serializer.save()

        # Criar a Solicitação de Atendimento associada ao Caso Clínico
        models.SolicitacaoAtendimento.objects.create(
            paciente=caso_clinico.paciente,
            fisioterapeuta=caso_clinico.servico_fisioterapeuta.fisioterapeuta,
            servico=caso_clinico.servico_fisioterapeuta.servico,
            caso_clinico=caso_clinico
        )

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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user

        if user.user_type == 'FIS':
            return models.SolicitacaoAtendimento.objects.filter(fisioterapeuta=user)

        if user.user_type == 'PAC':
            return models.SolicitacaoAtendimento.objects.filter(paciente=user)

        return models.Serializers.SolicitacaoAtendimento.objects.none()

    def perform_create(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = request.data.get('status', instance.status)
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)