from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.conf import settings

from .forms import RegisterForm, UpdateProfileForm
from .models import CustomUser


# HOME PAGE
def home_view(request):
    return redirect('login')


# REGISTER VIEW
def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # Default role
            user.role = 'student'

            user.email = form.cleaned_data['email']

            user.save()

            # Welcome Email
            send_mail(
                'Welcome to School Management System',
                f'Hello {user.full_name}, Welcome to our School Management System.',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )

            login(request, user)

            return redirect('profile')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


# LOGIN VIEW
def login_view(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile')

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


# LOGOUT VIEW
def logout_view(request):
    logout(request)
    return redirect('login')


# PROFILE VIEW
@login_required
def profile_view(request):

    return render(request, 'profile.html')


# EDIT PROFILE
@login_required
def edit_profile(request):

    if request.method == 'POST':

        form = UpdateProfileForm(request.POST, instance=request.user)

        if form.is_valid():

            form.save()

            # Email after profile update
            send_mail(
                'Profile Updated Successfully',
                'Your profile has been updated successfully.',
                settings.EMAIL_HOST_USER,
                [request.user.email],
                fail_silently=False,
            )

            return redirect('profile')

    else:
        form = UpdateProfileForm(instance=request.user)

    return render(request, 'edit_profile.html', {'form': form})


# TEACHER DASHBOARD
@login_required
def teacher_dashboard(request):

    if request.user.role != 'teacher':
        return redirect('profile')

    students = CustomUser.objects.filter(role='student')

    return render(request, 'teacher_dashboard.html', {'students': students})


# DELETE STUDENT
@login_required
def delete_student(request, id):

    if request.user.role != 'teacher':
        return redirect('profile')

    student = get_object_or_404(CustomUser, id=id)

    student.delete()

    return redirect('teacher_dashboard')


# TOGGLE STUDENT STATUS
@login_required
def toggle_student_status(request, id):

    if request.user.role != 'teacher':
        return redirect('profile')

    student = get_object_or_404(CustomUser, id=id)

    student.is_active_student = not student.is_active_student

    student.save()

    return redirect('teacher_dashboard')