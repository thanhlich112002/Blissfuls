from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    # //    path('login/', views.MyLoginView.as_view(template_name='user/login.html'), name='login'),
    path('main', views.main, name='main'),
    path('detail<int:id>', views.detailUser, name='detailuser'),
    path('detail_id<int:id>', views.detailUser_id, name='detailuser_id'),
    path('load_dsnv<int:id>', views.load_DSNV, name='load_DSNV'),
    path('add_nv', views.add_nv, name='add_nv'),
    path('themnhanvien', views.themnhanvien, name='themnhanvien'),
    path('delete<int:id>', views.delete, name='delete'),
    path('update<int:id>', views.update, name='update'),
    path('', views.dangnhap, name='checkdangnhap'),
    path('dsnv_name<int:id>', views.dsnv_name, name='dsnv_name'),
    path('body', views.body, name='body'),
    path('logout', views.my_logout, name='logout'),
]
