from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.core.paginator import Paginator
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail


# Show all students with Search + Filter + Pagination
def student_list(request):

    students = Student.objects.all().order_by('-date_added')

    # Search
    search_query = request.GET.get('search')

    if search_query:
        students = students.filter(
            Q(name__icontains=search_query) |
            Q(id__icontains=search_query) |
            Q(student_class__icontains=search_query) |
            Q(address__icontains=search_query)
        )

    # Filter by Date Added
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        students = students.filter(
            date_added__date__range=[start_date, end_date]
        )

    # Pagination
    paginator = Paginator(students, 5)  # 5 students per page

    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)

    context = {
        'students': students,
    }

    return render(request, 'student_list.html', context)


# Add student
def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        student_class = request.POST.get('student_class')
        email = request.POST.get('email')
        date_of_birth = request.POST.get('date_of_birth')
        address = request.POST.get('address')
        image = request.FILES.get('image')

        student = Student.objects.create(
            name=name,
            student_class=student_class,
            email=email,
            date_of_birth=date_of_birth,
            address=address,
            image=image
        )

        subject = 'Welcome to Student Management System'
        message = (
            f'Hello {student.name},\n\n'
            'Welcome to Student Management System.\n\n'
            'Your student details are:\n'
            f'Name: {student.name}\n'
            f'Class: {student.student_class}\n'
            f'Email: {student.email}\n'
            f'Date of Birth: {student.date_of_birth}\n'
            f'Address: {student.address}\n\n'
            'Thank you.'
        )

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [student.email],
            fail_silently=False,
        )

        return redirect('student_list')

    return render(request, 'add_student.html')


# Update student
def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.student_class = request.POST.get('student_class')
        student.email = request.POST.get('email')
        student.date_of_birth = request.POST.get('date_of_birth')
        student.address = request.POST.get('address')

        if request.FILES.get('image'):
            student.image = request.FILES.get('image')

        student.save()

        return redirect('student_list')

    return render(request, 'update_student.html', {'student': student})


# Delete student
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'delete_student.html', {'student': student})
