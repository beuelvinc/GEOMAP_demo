from django.shortcuts import render
from .models import Person
# Create your views here.
def home(request):
	context=Person.objects.all()
	return render(request,'home.html',{'context':context})

def baser(request):
	return render(request,'baser.html')
