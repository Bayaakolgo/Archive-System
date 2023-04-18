from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import NewUserForm,UploadForm, LoginForm
from .models import Upload
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/login/")
def delete_request(request, pk):
    document = get_object_or_404(Upload, pk=pk)
    document.delete()
    return redirect('dashboard')

@login_required(login_url="/login/")
def download_request(request, pk):
    document = get_object_or_404(Upload, pk=pk)
    response = HttpResponse(document.file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{document.file.name}"'
    return response

@login_required(login_url="/login/")
def upload_request(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect("dashboard") 
    else:
        form = UploadForm()

    return render(request, "main/upload.html", {
        "form": form
    })

@login_required(login_url="/login/")
def dashboard_request(request):
    uploads = Upload.objects.all()
    context = {'uploads':uploads}
    return render(request, 'main/index.html', context=context)

def logout_request(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('login')

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            messages.success(request, 'Registration successfull.')
            return redirect('login')
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')
    else:
        form = NewUserForm()

    return render(request=request, template_name='main/register.html', context={'form':form})

def login_request(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    form = LoginForm()

    return render(request=request, template_name='main/login.html', context={'form':form})