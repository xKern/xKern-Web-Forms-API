from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from job import views

urlpatterns = [
    path('job', views.JobList.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
