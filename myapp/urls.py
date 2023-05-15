from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('citizen/', views.citizen, name='citizen'),
    path('otp/', views.otp, name='otp'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('password/', views.password, name='password'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('view-profile/', views.view_profile, name='view-profile'),
    path('add-FIR/', views.add_FIR, name='add-FIR'),
    path('view-FIR/', views.view_FIR, name='view-FIR'),
    path('view-one-FIR/<int:pk>', views.view_one_FIR, name='view-one-FIR'),
    path('search-station/', views.search_station, name='search-station'),
    path('add-com/', views.add_com, name='add-com'),
    path('feedback/', views.feedback, name='feedback'),
    path('view-com/', views.view_com, name='view-com'),
    path('view-one-com/<int:pk>', views.view_one_com, name='view-one-com'),
    path('emergency/', views.emergency, name='emergency'),
    path('rules/', views.rules, name='rules'),
    path('missing/', views.missing, name='missing'),
    path('missing-one/<int:pk>', views.missing_one, name='missing-one'),


]
