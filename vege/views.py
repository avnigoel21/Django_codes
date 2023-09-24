from django.shortcuts import render , redirect
from .models import *
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
    context = {'receipes' : queryset}


    return render (request , 'receipes/receipes.html' , context )



def delete_receipes(request, id):
    return redirect('receipes/')

def update_receipes(request, id):
    return redirect('receipes/')


