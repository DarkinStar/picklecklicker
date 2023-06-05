from django.urls import path
from .views import ( 
    register, 
    user_login, 
    user_logout,
    increase_total_count, 
    get_total_count,
    inc_click_boost,
    auto_increase,
    buy_auto_click
)


app_name = 'backend'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('increase/', increase_total_count, name='increase'),
    path('get/', get_total_count, name='get'),
    path('increase_boost/', inc_click_boost, name="increase_boost"),
    path('auto_increase/', auto_increase, name='auto_increase'),
    path('buy_auto_click/', buy_auto_click, name='buy_auto_click'),
]
