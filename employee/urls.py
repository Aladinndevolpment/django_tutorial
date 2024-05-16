from rest_framework.routers import DefaultRouter
from .views import EmployeeProfileViewSet, AllEmployeeViewSet

router = DefaultRouter()
# TODO: complete route
router.register('profile', EmployeeProfileViewSet, basename='employee')

router.register('get-all-employees', AllEmployeeViewSet,
                basename='all_employees')

urlpatterns = router.urls
