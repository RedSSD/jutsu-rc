from django.urls import path
from . import views

urlpatterns = [
    path('update/', views.telegram_bot, name='telegram_bot'), #new
]
