from rest_framework.routers import DefaultRouter
from django.urls import path
from lms.views import EmployeeViewSet, LeadViewSet, GenerateToken, EmployeeAPIView

router = DefaultRouter()
router.register('employee', EmployeeViewSet, basename='api_employee')
router.register('lead', LeadViewSet, basename='api_lead')


urlpatterns = router.urls + [
    path('auth/', GenerateToken.as_view()),
    path('me/', EmployeeAPIView.as_view())
]
