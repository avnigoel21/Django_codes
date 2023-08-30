from django.shortcuts import render
from django.http import HttpResponse


def home(request):

    text = 'hi i am backend text' 

    peoples = [
        {'name' : 'Aditi'  , 'age' : 26},
        {'name' : 'Harry'  , 'age' : 18},
        {'name' : 'Vicky'  , 'age' : 16},
        {'name' : 'Sandeep'  , 'age' : 30},
    ]

    # for people in peoples:
    #     print(people)
        
    return render(request , 'home/index.html' , context={'text' : text , 'peoples' : peoples })


def success_page(request):
    print("hello world")
    print("*" * 10)
    return HttpResponse("Hey this is success page.")



