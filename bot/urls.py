from django.urls import path
from . import views

urlpatterns = [
    path('update/', views.telegram_bot_handler, name='telegram_bot_handler'), #new
]
