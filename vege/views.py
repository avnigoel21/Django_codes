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


