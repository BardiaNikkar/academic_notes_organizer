from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NoteForm
from .models import Note
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

@login_required
def note_list(request):
     notes = Note.objects.filter(user=request.user).select_related('course').order_by('-created_at')
     return render(request, 'notes/note_list.html', {'notes':notes})

@login_required
def update_note(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        form.fields['course'].queryset = Course.objects.filter(user=request.user)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
        form.fields['course'].query = Course.objects.filter(user=request.user)
    return render(request, 'notes/note_update.html', {'form':form, 'note':note})

@login_required
def delete_note(request, pk):
     note = get_object_or_404(Note, pk=pk, user=request.user)
     if request.method == "POST":
          note.delete()
          return redirect('note_list')
     return render(request, 'notes/note_delete.html', {'note':note})
