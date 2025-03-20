from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee,CustomUser,Report
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import CustomUserCreationForm,CustomUserChangeForm


class EmployeeListView(LoginRequiredMixin,ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'
    paginate_by = 10

class EmployeeCreateView(LoginRequiredMixin,CreateView):
    model = Employee
    template_name = 'employees/employee_form.html'
    fields = ['first_name', 'last_name', 'position', 'phone_number', 'email', 'hire_date']
    success_url = reverse_lazy('employee-list')

class EmployeeUpdateView(LoginRequiredMixin,UpdateView):
    model = Employee
    template_name = 'employees/employee_form.html'
    fields = ['first_name', 'last_name', 'position', 'phone_number', 'email', 'hire_date']
    success_url = reverse_lazy('employee-list')

class EmployeeDeleteView(LoginRequiredMixin,DeleteView):
    model = Employee
    template_name = 'employees/employee_confirm_delete.html'
    success_url = reverse_lazy('employee-list')





class UserListView(LoginRequiredMixin,ListView):
    model = CustomUser
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    paginate_by = 10

class UserCreateView(LoginRequiredMixin,CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('user-list')

class UserUpdateView(LoginRequiredMixin,UpdateView):
    form_class = CustomUserChangeForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('user-list')
    
class UserDeleteView(LoginRequiredMixin,DeleteView):
    model = CustomUser
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('user-list')





class ReportListView(LoginRequiredMixin,ListView):
    model = Report
    template_name = 'reports/report_list.html'
    context_object_name = 'reports'

class ReportCreateView(LoginRequiredMixin,CreateView):
    model = Report
    template_name = 'reports/report_form.html'
    fields = ['report_type', 'content']
    success_url = reverse_lazy('report-list')
    def form_valid(self, form): # new
        form.instance.generated_by = self.request.user
        return super().form_valid(form)

class ReportUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Report
    template_name = 'reports/report_form.html'
    fields = ['report_type', 'content']
    success_url = reverse_lazy('report-list')

    def test_func(self): # new
        obj = self.get_object()
        return obj.generated_by == self.request.user

class ReportDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Report
    template_name = 'reports/report_confirm_delete.html'
    success_url = reverse_lazy('report-list')

    def test_func(self):
        obj = self.get_object()
        return obj.generated_by == self.request.user

