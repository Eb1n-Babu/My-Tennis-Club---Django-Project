from django.urls import path
from .views import member,details,main,test,add_member,test2,test3,test4
urlpatterns = [
    path('',main,name='main'),
    path('members/', member,name='members'),
    path('members/details/<id>', details,name='details'),
    path('test/',test,name='test'),
    path('add_member/',add_member,name='add_member'),
    path('test2/',test2,name='test2'),
    path('test3/',test3,name='test3'),
    path('test4/',test4,name='test4'),
]
