from django.shortcuts import render
from rest_framework.views import APIView ## django에서 Rest Framework사용하는 라이브러리 불러옴

""" 이 sub이라는 class를 실행할 때
GET으로 호출한다고 하면 def get 이 실행이 된다."""
class Sub(APIView):
    def get(self, request):
        print("GET으로 호출")
        return render(request, 'hoonstagram/main.html')

    def post(self, reqeust):
        print("POST로 호출")
        return render(reqeust, 'hoonstagram/main.html')