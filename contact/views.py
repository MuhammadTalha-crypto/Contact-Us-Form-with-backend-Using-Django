from django.shortcuts import render
# from . import 
from contact.models import data
# Create your views here.
def index(request):
    return render(request, 'index.html')
def contact(request):
    #Below program will run when the form will be submitted using method "POST"
    if request.method == 'POST':
        #requesting value from contact us form (which uses method POST) against "name" using .get dictionary. 
        name = request.POST.get('name')         
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        #Creating an object with all the values for data base
        contact = data(name= name, desc= desc, email = email)
        #Saving the object in the database.
        contact.save()
        #rendering the template "contact.html" from templates folder
    return render(request, 'contact.html')