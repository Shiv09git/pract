from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
def setcookie(request):
    sc = HttpResponse('COOKIES SET')
    sc.set_cookie("month","April")
    sc.set_cookie("Course","Python", max_age=4)
    return sc

def getcookie(request):
    gc = request.COOKIES.get("month")
    getc = HttpResponse(f"GET COOKIE:{gc}")
    return getc

def deletecookie(request):
    dc = HttpResponse("Delete Cookies")
    dc.delete_cookie('month')
    return dc
