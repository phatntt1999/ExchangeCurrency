from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.index, name='contact'),
    path('blog/', views.blog, name='blog')

]
