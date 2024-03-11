"""
URL configuration for start project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from . import views


urlpatterns = [
  path('home',views.home,name='home'),
  path('social-auth/', include('social_django.urls', namespace='social')),
  path('viewc',views.viewc,name='viewc'),
  path('viewf',views.viewf,name='loginf'),
  path('views',views.search_hotels,name='loginfs'),
  path('viewa',views.add_person,name='add'),
  path('viewa',views.add_person,name='add'),
  path('home2',views.home2,name='home2'),
  path('login1',views.login1,name='login1'),
    path('flights1',views.flights1,name='vyoma'),
    path('trips',views.trips,name='vyoma'),
    path('add_trip',views.add_trip,name="add_trip"),
    path('info/<int:trip_id>/',views.trip_info1,name='view_trip'),
    path('infoe/<int:event_id>/',views.event_info,name='infoe'),
    path('d_info/<int:event_id>/',views.event_info1,name='d_info'),
    path('add_plan',views.add_plan,name="add_plan"),
    path('add_event',views.add_event,name="add_event"),
    path('edit_profile/<str:profile_id>',views.edit_profile,name="edit_profile"),
    path('users/<int:trip_id>',views.trip_detail,name="trip_deatil"),
    #path('add_expense/<int:trip_id>',views.add_expense,name="add_expense"),
    path('add_expense1',views.add_expense1,name="add_expense"),
    path('add_friends',views.add_friends,name="add_friends"),
    path('expense/<int:trip_id>',views.expense1,name="expense"),
    path("logout",views.logout1,name="logout"),
    path("try",views.try1,name="try1"),
    path('a_follow/<int:event_id>/',views.follow,name='a_follow'),
    


]
