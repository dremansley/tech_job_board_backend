from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_jobs, name='job_list'),
    path('jobs/create/', views.create_job_listing, name='job_create'),
]
