"""Hoonstagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import Sub

# Sub.as_view()가 무슨 뜻인가요?! -> 우리가 그냥 생 URL로 실행을 한다면 Sub class를 view로 사용하겠다. 는 뜻이기에
# path(a, b) b자리에는 무조건 view가 들어와야하기 때문에 __ 더 자세히 알고 싶으시다면 들어가서 확인해봐라!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',Sub.as_view() ), # 아무것도 없이 들어왔을 경우에는 뭘 할 것인가? 즉 "127.0.0.1:8000" 일 때 보여지는 template

]
