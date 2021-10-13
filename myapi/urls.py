"""myapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from myapi.myapp.models import employee
from django.contrib import admin
from django.urls import path
# import some 
from rest_framework.urlpatterns import format_suffix_patterns
from myapp import views
# authentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    
     # class Base API
    path('',views.class_Base_API.as_view()),
    path('<int:pk>/',views.class_Base_API.as_view()),

    # authentication
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='refresh_token'),
    path('verifytoken/',TokenVerifyView.as_view(),'verfy_token'),


]
