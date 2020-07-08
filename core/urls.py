from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from core import views


router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView, 'task')

urlpatterns = [
    path('api/', include(router.urls))
]
