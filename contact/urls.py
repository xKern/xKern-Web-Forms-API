from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from contact import views

urlpatterns = [
    path('contact', views.ContactList.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
