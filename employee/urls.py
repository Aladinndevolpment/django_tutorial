from rest_framework.routers import DefaultRouter
from .views import EmployeeProfileViewSet

router = DefaultRouter()
# TODO: complete route
router.register('profile', EmployeeProfileViewSet, basename='employee')

urlpatterns = router.urls
