"""xkern_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.models import User, Group

admin.site.site_header = "xKern"
admin.site.site_title = "Admin portal"
admin.site.index_title = "xKern"
admin.site.unregister(User)
admin.site.unregister(Group)


urlpatterns = [
    path('api/', include('contact.urls')),
    path('api/', include('job.urls')),
    path('admin/', admin.site.urls),
]
