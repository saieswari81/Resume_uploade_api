from django.urls import path
from . import views

urlpatterns = [
    path('resume/', views.ProfileAPIView.as_view(), name='resume'),
]

