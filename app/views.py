from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import ToDo
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TaskForm,UpdateForm
from django.contrib.auth import login,authenticate,logout 
# Create your views here.


@login_required(login_url='login')
def home_view(request):


	obj = ToDo.objects.filter(user=request.user)
	form = TaskForm(request.POST  or None)
	done = ToDo.objects.filter(user=request.user,completed=True)
	not_done = ToDo.objects.filter(user=request.user,completed=False)
	percentage = int((len(done)/len(not_done))*100)
	

	if form.is_valid():
		xy = form.save(commit=False)
		xy.user = request.user
		form.save()
		form = TaskForm()
	context = { 
		'items':obj,'form':form,'per':percentage,'done':done,'not':not_done
	}



	return render(request,'app/home.html',context)

@login_required(login_url='login')
def update_page(request,id):
	obj = ToDo.objects.get(id=id)
	form = UpdateForm(request.POST or None,instance=obj)
	if form.is_valid():
		form.save()
		return redirect("home")
	context = {'form':form}
	template_name = "app/update.html"
	return render(request,template_name,context)

@login_required(login_url='login')
def delete_view(request,id):
	work = ToDo.objects.get(id=id)
	print(work.task)
	if request.method == "POST":
		work.delete()
		return redirect("home")
	
	context = {
		'task':work
	}
	template_name = 'app/delete.html'
	return render(request,template_name,context)

def register_page(request):
	if request.method == "POST":
		username = request.POST['Username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		if password1 == password2:
			user = User.objects.create_user(username=username,password=password1,email=email)
			user.save()
			return redirect('login')
		else:
			messages.info(request,"Two passwords are not matching")
			

			
	context = {}
	return render(request,"app/register.html",context)


def login_page(request):

	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect("home")
		else:
			messages.info(request,"username or password is incorect")

	context = {}

	return render(request,"app/login.html",context)

	
def logout_page(request):
	logout(request)
	return redirect("home")


