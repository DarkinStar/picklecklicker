from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from backend.models import Clicker, User
from django.contrib.auth.forms import UserCreationForm

@login_required
def game(request):
    return render(request, 'frontend/game.html')

