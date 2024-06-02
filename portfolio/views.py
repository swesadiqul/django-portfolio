from django.shortcuts import render
from .models import*

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        user = Contact(name=name, email=email, message=message)
        user.save()

    return render(request, 'index.html')