from rest_framework.routers import  DefaultRouter
from clinica import viewsets

router = DefaultRouter()
router.register('paciente', viewsets.PacienteViewSet)

router.register('fisioterapeuta', viewsets.FisioterapeutaViewSet)

router.register('servico', viewsets.ServicoViewSet)

router.register('caso_clinico', viewsets.CasoClinicoViewSet)

urlpatterns = router.urls