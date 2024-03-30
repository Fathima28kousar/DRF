from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('generic-student/',StudentGeneric.as_view()),
    path('generic-student/<id>/',StudentGeneric1.as_view())

    # #path('',home,name='home'),
    # #path('students',post_student,name='students'),
    # #path('update_student/<id>',update_student,name='update_student'),
    # path('student/',StudentAPI.as_view()),
    # path('get_book',get_book,name='get_book'),
    # path('register',RegisterUser.as_view()),
    
]