from django.shortcuts import render , redirect
from .models import *

from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth import authenticate, login


# Create your views here.

def receipes(request):


    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        # print(receipe_name)
        # print(receipe_description)
        
        Recipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )

        return redirect('/receipes')

    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))


    context = {'receipes' : queryset}


    return render (request , 'receipes/receipes.html' , context )



def delete_receipes(request, id):

    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes')

def update_receipes(request, id):


    queryset = Recipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image :
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipes')
    
    context = {'receipe' : queryset}

    return render (request , 'receipes/update_receipes.html' , context )



def login_page(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username")
            return redirect("/login/")
        
        user = authenticate(username = username , password = password)

        if user is None:
            messages.error(request, "Invald Password")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/receipes")

    return render(request, 'receipes/login.html')


def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username already taken") 
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account created successfully")

        return redirect('/register/')

    return render(request, 'receipes/register.html')


