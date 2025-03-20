from django.urls import path
from .views import (EmployeeListView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView,
    UserListView, UserCreateView, UserUpdateView, UserDeleteView,
    ReportListView, ReportCreateView, ReportUpdateView, ReportDeleteView,)

from django.contrib.auth import views as auth_views



urlpatterns = [
    
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('employees/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employees/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee-delete'),

    # User URLs
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),

    # Report URLs
    path('reports/', ReportListView.as_view(), name='report-list'),
    path('reports/create/', ReportCreateView.as_view(), name='report-create'),
    path('reports/<int:pk>/update/', ReportUpdateView.as_view(), name='report-update'),
    path('reports/<int:pk>/delete/', ReportDeleteView.as_view(), name='report-delete'),

]