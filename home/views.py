from django.shortcuts import render, redirect
from django.http import HttpResponse

from  .utils import send_mail_to_client, send_email_with_attachment
from django.conf import settings


# def send_email(request):
#     send_mail_to_client()
#     return redirect('/')

def send_email(request):
    subject = "This email if from django server with Attachment"
    message = "Hey, please find this attach file with this email"
    recipent_list = ["avnigoel98@gmail.com" , 'achimote2021@gmail.com']
    file_path = f"{settings.BASE_DIR}/main.xlsx"
    send_email_with_attachment(subject, message, recipent_list, file_path)
    return redirect('/')


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
