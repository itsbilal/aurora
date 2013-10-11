# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

class login(View):
    def get(self,request):
    	return render(this, "login.html")

    def post(self,request):
    	if request.user.is_authenticated:
    		logout()

    	username = request.POST["username"]
    	password = request.POST["password"]

    	user = authenticate(username,password)

    	if user is not None:
    		if user.is_active:
    			login(request, user)
    			return HttpResponseRedirect("/")

    	res = HttpResponse("401 Unauthorized")
    	res.status_code = 401
    	return res

