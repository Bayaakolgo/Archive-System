from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import NewUserForm
from .models import Upload
from .forms import UploadForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def delete_request(request, pk):
    document = get_object_or_404(Upload, pk=pk)
    document.delete()
    return redirect('dashboard')

@login_required
def download_request(request, pk):
    document = get_object_or_404(Upload, pk=pk)
    response = HttpResponse(document.file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{document.file.name}"'
    return response

@login_required
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

@login_required
def dashboard_request(request):
    uploads = Upload.objects.all()
    context = {'uploads':uploads}
    return render(request, 'main/dashboard.html', context=context)

def logout_request(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('login')

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successfull.')
            return redirect('login')
        messages.error(request, 'Unsuccessful registration. Invalid information.')
    form = NewUserForm()
    return render(request=request, template_name='main/register.html', context={'register_form':form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
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
    form = AuthenticationForm()
    return render(request=request, template_name='main/login.html', context={'login_form':form})