from django.urls import path
from . import views
urlpatterns = [
    path('ins-login/', views.ins_login,name='ins-login'),
    path('ins-index/',views.ins_index,name='ins-index'),
    path('ins-view-FIR/',views.ins_view_FIR,name='ins-view-FIR'),
    path('ins-view-one-FIR/<int:pk>',views.ins_view_one_FIR,name='ins-view-one-FIR'),
    path('ins-view-com/',views.ins_view_com,name='ins-view-com'),
    path('ins-view-one-com/<int:pk>',views.ins_view_one_com,name='ins-view-one-com'),
    path('ins-manage-com/',views.ins_manage_com,name='ins-manage-com'),
    path('ins-disable/<int:pk>',views.ins_disable,name='ins-disable'),
    path('ins-enable/<int:pk>',views.ins_enable,name='ins-enable'),
    path('ins-manage-view/<int:pk>',views.ins_manage_view,name='ins-manage-view'),
    path('ins-edit-profile/',views.ins_edit_profile,name='ins-edit-profile'),
    path('ins-view-profile/',views.ins_view_profile,name='ins-view-profile'),
    path('ins-change-password/',views.ins_password,name='ins-change-password'),
]