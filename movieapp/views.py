from django.shortcuts import render
from .forms import MovieForm
from .models import Movie
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def register(request):
	form=MovieForm(request.POST,request.FILES)
	if form.is_valid():
		form.save()
		messages.success(request,request.POST['moviename']+'is added successfully')
	form=MovieForm()
	return render(request,'register.html',{'form':form})

def show(request):
	data=Movie.objects.all()
	return render(request,'show.html',{'data':data})