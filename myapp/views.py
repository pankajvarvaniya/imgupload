from django.shortcuts import render,redirect
from .forms import Myimage
from .models import Image
# Create your views here.

def home(request):
	if request.method=='POST':
		form=Myimage(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			print('hello00000000000000000')

	form=Myimage()
	img=Image.objects.all()
	return render(request,'myapp/home.html',{'form':form,'img':img})

def delete(request,id):
	image=Image.objects.get(id=id)
	image.delete()
	return redirect('home')
