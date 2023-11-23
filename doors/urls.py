from django.urls import path

from doors import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/<int:pk>', views.detail, name='detail'),
    path('catalog', views.catalog, name='catalog'),
    path('contacts', views.contacts, name='contacts')
]
