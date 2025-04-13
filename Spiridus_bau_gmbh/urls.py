from django.urls import path
from . import views


app_name = 'Spiridus_bau_gmbh'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_form_view, name='contact'),  # здесь и форма, и отправка
    path('referenzen/', views.referenzen, name='referenzen'),
    path('offene_stellen/', views.offene_stellen, name='offene_stellen'),
    path('datenschutz/', views.datenschutz, name='datenschutz'),
    path('impressum/', views.impressum, name='impressum'),
    path('umbau/', views.umbau, name='umbau'),
    path('schalung/', views.schalung, name='schalung'),
]





