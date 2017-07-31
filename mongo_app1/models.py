from django.db import models
from mongoengine import *
from MongoWeb.settings import DBNAME

connect(DBNAME)


class Employee(Document):
    name = StringField(max_length= 50)
    age = IntField(required=False)

jacky = Employee(name="Jacky",age="25")
jacky.save()

'''
class Post(Document):
    title = StringField(max_length=120,required=True)
    content = StringField(max_length=500,required=True)
    last_update = DateTimeField (required= True)
'''