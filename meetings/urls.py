"""
URL configuration for meetings_planner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path

from meetings.views import addmeeting, deletemeeting, detail, meeting_list

urlpatterns = [
    path('', meeting_list,name='meetings'),
    path('detail/<int:id>/', detail ,name='detail'),
    path('delete/<int:id>/',deletemeeting,name='deletemeeting'),
    path('add/',addmeeting,name='addmeeting'),
]
