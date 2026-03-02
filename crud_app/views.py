from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Student
from .forms import StudentForm

# Redirect home to login page if not logged in
def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('student_list')
    else:
        return redirect('login')


@login_required
def student_list(request):
    query = request.GET.get('q', '')
    if query:
        students = Student.objects.filter(
            Q(name__icontains=query) |
            Q(study__icontains=query) |
            Q(city__icontains=query)
        )
    else:
        students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students, 'query': query})


@login_required
def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'form': form})


@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'form': form})


@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')