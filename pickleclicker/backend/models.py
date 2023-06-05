from django.db import models
from django.contrib.auth.models import User



class Clicker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_count = models.IntegerField(default=0)
    click_boost = models.IntegerField(default=1)
    click_per_sec = models.IntegerField(default=0)
    click_boost_inc_cost = models.IntegerField(default=10)
    click_per_sec_inc_cost = models.IntegerField(default=50)
