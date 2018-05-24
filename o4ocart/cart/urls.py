from django.urls import path

from . import views

urlpatterns = [
    path('user_getinfo/', views.user_getinfo, name='user_getinfo'),
    #path('', views.user_getinfo, name='user_getinfo'),
    path('cart_add/', views.cart_add, name='cart_add'),
    path('ad_add/', views.ad_add, name='ad_add'),
    path('coupon_add/', views.coupon_add, name='coupon_add'),
    path('camera_add/', views.camera_add, name='camera_add'),

]