"""withrestc3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path
from testApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #re_path('api/', views.EmployeeListApiView.as_view()),
    #re_path(r'api/(?P<pk>\d+)/$', views.EmployeeRetrieveAPIView.as_view()),
    #re_path('api/', views.EmployeeCreateAPIView.as_view()),
    #re_path(r'api/(?P<pk>\d+)/$', views.EmployeeUpdateAPIView.as_view()),
    #re_path(r'api/(?P<pk>\d+)/$', views.EmployeeDestroyAPIView.as_view()),
    #re_path(r'api/$', views.EmployeeListCreateAPIView.as_view()),
    #re_path(r'api/(?P<pk>\d+)/$', views.EmployeeRetriveUpdateAPIView.as_view()),
    #re_path(r'api/(?P<pk>\d+)/$', views.EmployeeRetriveDestroyAPIView.as_view()),
    #re_path(r'api/(?P<pk>\d+)/$', views.EmployeeRetriveUpdateDestroyAPIView.as_view()),
    #re_path(r'api', views.EmployeeListCreateModelMixin.as_view()),
    re_path(r'api/(?P<pk>\d+)', views.EmployeeRetrieveUpdateDestroyModelMixin.as_view()),
]
