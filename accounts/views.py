from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from courses.models import Course
from notes.models import Note

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", { 'form' : form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form' : form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    courses = Course.objects.filter(user=request.user).prefetch_related('notes')
    notes_count = Note.objects.filter(user=request.user).count()
    return render(request, 'accounts/dashboard.html', {'courses':courses, 'notes_count': notes_count})
