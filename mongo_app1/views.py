from django.shortcuts import render
from django.http import  HttpResponse
from mongoengine import  connect
from MongoWeb.settings import DBNAME
from mongo_app1.models import Employee

connect(DBNAME)

# Create your views here.
def homepage(request):
    html = "hello"
    posts = Employee.objects.all()
    posts_lists = list()

    for post in posts :
        posts_lists.append(post["name"]+"<br>")

    return HttpResponse(posts_lists)