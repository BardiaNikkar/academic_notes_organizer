from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NoteForm
from courses.models import Course

# Create your views here.
# to create this view function I got help from chatgpt

@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        form.fields['course'].queryset = Course.objects.filter(user = request.user)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_list')
    else:
            form = NoteForm()
            form.fields['course'].queryset = Course.objects.filter(user=request.user)
    return render(request, 'notes/note_create.html', {'form':form})
    