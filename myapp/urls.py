
from django.urls import path,include
from rest_framework import routers
from myapp.views import CompanyViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register(r'companys', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls) ),
]