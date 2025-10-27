from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('v1/api/', include('resumes.urls')),
]
