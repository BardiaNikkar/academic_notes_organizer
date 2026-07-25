from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CourseForm

# Create your views here.

@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.user = request.user
            course.save()
            return redirect("dashboard")
    else:
        form = CourseForm()
    return render(request, 'courses/course_create.html', {'form':form})
