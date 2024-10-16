from rest_framework.routers import  DefaultRouter
from clinica import viewsets

router = DefaultRouter()
router.register('usuario', viewsets.UserViewSet)

router.register('servico', viewsets.ServicoViewSet)

router.register('caso_clinico', viewsets.CasoClinicoViewSet)

router.register('servico_fisioterapeuta', viewsets.ServicoFisioterapeutaViewSet)

router.register('solicitacao_atendimento', viewsets.SolicitacaoAtendimentoViewSet)

urlpatterns = router.urls