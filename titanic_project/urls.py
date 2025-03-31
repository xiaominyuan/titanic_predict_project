from django.urls import path
from . import views

urlpatterns = [
    path('titanic_sync/', views.titanic_sync),
    path('titanic_async/', views.titanic_async),
    path('titanic_result/<str:job_id>/', views.titanic_result),
    path('test_alive', views.test_alive),

]
