from django.shortcuts import render

def student_list(request):
    return render(request, 'student.html')