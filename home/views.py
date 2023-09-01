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

    vegetables = ['pumpkin' , 'tomato' , 'potato']

    # for people in peoples:
    #     print(people)
        
    return render(request , 'home/index.html' , context={'text' : text , 'peoples' : peoples , 'vegetables' : vegetables })


def success_page(request):
    print("hello world")
    print("*" * 10)
    return HttpResponse("Hey this is success page.")


def contact(request):
    return render(request , 'home/contact.html')

def about(request):
    return render(request , 'home/about.html')
