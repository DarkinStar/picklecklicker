from django.urls import path
from .views import (game,
)

app_name = 'frontend'

urlpatterns = [
    path('', game, name='game')
]
