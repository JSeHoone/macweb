from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
class PayPlan(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

## 이렇게 만들면 한 테이블에 쌓이고
class Users(AbstractUser):
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING) ## 현재 가지고 있는 유저를 가지고 Pay_plan을 넣겠다 


## 이렇게 만들면 두 테이블에 쌓인다
class UserDetail(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE) # 유저가 가지고 있는 추가 정보를 여기에 넣겠다는 의미 
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)