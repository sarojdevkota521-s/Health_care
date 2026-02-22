from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, DoctorViewSet, MappingViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patients')
router.register(r'doctors', DoctorViewSet, basename='doctors')
router.register(r'mappings', MappingViewSet, basename='mappings')

urlpatterns = router.urls