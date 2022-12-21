from django.http.response import JsonResponse
# from shortner.models import Users
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
    print(request.FILES)
    return render(request, "index.html" )

# def drag_drop(request):
#     return(request, "drag_drop.html")

# def index(request):
#     user = Users.objects.filter(username = 'admin').first()
#     email = user.email if user else "없는 회원"
#     print(email)
#     print(request.user.is_authenticated)
#     if request.user.is_authenticated is False:
#         email = "없는 회원"
#     print(email)
#     return render(request, "base.html", {"welcome_msg" : "Hello JSH"}) # request(반응) , base html (어떤 템플릿을 보여줄 것인가?), 문구 보여 주는거 

# def redirect_test(request):
#     print('Go Redirect')
#     return redirect("index")

# @csrf_exempt # 
# def get_user(request, user_id):
#     print(user_id)
#     if request.method == "GET":
#         abc = request.GET.get("abc")
#         xyz = request.GET.get("xyz")
#         user = Users.objects.filter(pk = user_id).first()
#         return render(request , "base.html", {'user': user, 'params' : [abc,xyz]})

#     elif request.method == 'POST':
#         username = request.GET.get('username')
#         if username:
#             user = Users.objects.filter(pk=user_id).update(username=username)
#         return JsonResponse(dict(msg= "You just reached with Post Method!"))
