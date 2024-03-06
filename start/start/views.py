from django.shortcuts import render,HttpResponse,redirect
def hi(request):
    return redirect("blog/login1")