from rest_framework.routers import  DefaultRouter
from clinica import viewsets

router = DefaultRouter()
router.register('usuario', viewsets.UserViewSet)

router.register('servico', viewsets.ServicoViewSet)

router.register('caso_clinico', viewsets.CasoClinicoViewSet)

urlpatterns = router.urls