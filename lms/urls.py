from rest_framework.routers import DefaultRouter

from lms.views import EmployeeViewSet, LeadViewSet

router = DefaultRouter()
router.register('employee', EmployeeViewSet, basename='api_employee')
router.register('lead', LeadViewSet, basename='api_lead')

urlpatterns = router.urls
