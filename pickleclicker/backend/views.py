from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Clicker
from django.contrib.auth.forms import UserCreationForm



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            clicker = Clicker(user=user)
            clicker.save()
            login(request, user)
            return redirect('frontend:game')
    return render(request, 'frontend/register.html', context={"form": UserCreationForm()})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('frontend:game')
    return render(request, 'frontend/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('frontend:game')

@login_required
def increase_total_count(request):
    clicker = get_object_or_404(Clicker, user=request.user)
    clicker.total_count += clicker.click_boost
    clicker.save()
    res = {
        "total_count": clicker.total_count,
        "inc_value": clicker.click_boost,
        "click_per_sec_inc_cost": clicker.click_per_sec_inc_cost,
        "click_boost_inc_cost": clicker.click_boost_inc_cost
    }
    return JsonResponse(res)

@login_required
def get_total_count(request):
    clicker = get_object_or_404(Clicker, user=request.user)
    res = {
        "total_count": clicker.total_count,
        "inc_value": clicker.click_boost,
        "click_per_sec": clicker.click_per_sec,
        "click_per_sec_inc_cost": clicker.click_per_sec_inc_cost,
        "click_boost_inc_cost": clicker.click_boost_inc_cost

    }
    return JsonResponse(res)


@login_required
def inc_click_boost(request):
    clicker = get_object_or_404(Clicker, user=request.user)
    if clicker.total_count < clicker.click_boost_inc_cost:
        return JsonResponse(
            {"error": "No enough clicks to increase boost!"},
            status = 403
        )

    clicker.click_boost += 1
    clicker.total_count -= clicker.click_boost_inc_cost
    clicker.click_boost_inc_cost += 5
    clicker.save()
    res = {
        "total_count": clicker.total_count,
        "inc_value": clicker.click_boost,
        "click_per_sec_inc_cost": clicker.click_per_sec_inc_cost,
        "click_boost_inc_cost": clicker.click_boost_inc_cost
    }
    return JsonResponse(res)

@login_required
def auto_increase(request):
    clicker = get_object_or_404(Clicker, user=request.user)
    clicker.total_count += clicker.click_per_sec
    clicker.save()
    res = {
        "total_count": clicker.total_count,
        "click_per_sec": clicker.click_per_sec,
        "click_per_sec_inc_cost": clicker.click_per_sec_inc_cost,
        "click_boost_inc_cost": clicker.click_boost_inc_cost
    }
    return JsonResponse(res)
@login_required
def buy_auto_click(request):
    clicker = get_object_or_404(Clicker, user=request.user)
    if clicker.total_count < clicker.click_per_sec_inc_cost:
        return JsonResponse(
            {"error": "No enough clicks to buy auto click!"},
            status = 403
        )
    clicker.click_per_sec += 1
    clicker.total_count -= clicker.click_per_sec_inc_cost
    clicker.click_per_sec_inc_cost += 10
    clicker.save()
    res = {
        "total_count": clicker.total_count,
        "click_per_sec": clicker.click_per_sec,
        "click_per_sec_inc_cost": clicker.click_per_sec_inc_cost,
        "click_boost_inc_cost": clicker.click_boost_inc_cost
    }
    return JsonResponse(res)
