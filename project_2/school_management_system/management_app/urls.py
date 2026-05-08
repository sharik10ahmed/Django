from django.urls import path
from . import views

urlpatterns = [

    path('', views.home_view, name='home'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('profile/', views.profile_view, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),

    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),

    path('delete-student/<int:id>/', views.delete_student, name='delete_student'),

    path('toggle-status/<int:id>/', views.toggle_student_status, name='toggle_student_status'),
]