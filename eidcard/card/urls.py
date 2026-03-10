from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('generate/', views.generate_card, name='generate_card'),
    path('card/<int:card_id>/', views.card_detail, name='card_detail'),
]
