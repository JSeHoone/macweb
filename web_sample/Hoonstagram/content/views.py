from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed


# Create your views here.

class Main(APIView):
    def get(self, request):
        feed_list =  Feed.objects.all() # Feed의 객체들의 모든 것을 가져오겠다. // Quary Set // Select * From content_Feed;
    
        
        return render(request, "Hoonstagram/main.html", context=dict(feeds=feed_list))