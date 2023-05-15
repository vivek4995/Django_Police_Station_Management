from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('com-login/',views.com_login,name='com-login'),
    path('com-index/',views.com_index,name='com-index'),
    path('com-FIR/',views.com_FIR,name='com-FIR'),
    path('com-view-FIR/<int:pk>',views.com_view_FIR,name='com-view-FIR'),
    path('com-com/',views.com_com,name='com-com'),
    path('com-view-com/<int:pk>',views.com_view_com,name='com-view-com'),
    path('com-ins/',views.com_ins,name='com-ins'),
    path('com-man-ins/<int:pk>',views.com_man_ins,name='com-man-ins'),
    path('com-station',views.com_station,name='com-station'),
    path('com-view-station/<int:pk>',views.com_view_station,name='com-view-station'),
    path('com-con',views.com_con,name='com-con'),
    path('com-edit-profile/',views.com_edit_profile,name='com-edit-profile'),
    path('com-view-profile/',views.com_view_profile,name='com-view-profile'),
    path('com-change-password/',views.com_password,name='com-change-password'),



] 