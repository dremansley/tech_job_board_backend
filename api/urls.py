from django.urls import path
from .views import JobList, CreateJobListing

urlpatterns = [
    path('list/', JobList.as_view(), name='job_list'),
    path('jobs/create/', CreateJobListing.as_view(), name='job_create'),
]
