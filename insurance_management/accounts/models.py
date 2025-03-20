from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(models.Model):
    first_name = models.CharField(max_length=50,verbose_name='نام')
    last_name = models.CharField(max_length=50,verbose_name='نام خانوادگی')
    position = models.CharField(max_length=50,verbose_name='پست سازمانی')
    phone_number = models.CharField(max_length=15,verbose_name='شماره تماس')
    email = models.EmailField(max_length=100, unique=True,verbose_name='ایمیل')
    hire_date = models.DateField(verbose_name='تاریخ استخدام')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='ایجاد شده')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class CustomUser(AbstractUser):
    ROLES = [
        ('admin', 'ادمین'),
        ('employee', 'کارمند'),
    ]

    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='user', null=True, blank=True,verbose_name='کارمند')
    role = models.CharField(max_length=20, choices=ROLES, default='employee',verbose_name='نقش')

    def __str__(self):
        return self.username
    

class Report(models.Model):
    REPORT_TYPES = [
        ('financial', 'مالی'),
        ('claims', 'ادعاها'),
        ('policies', 'بیمه‌نامه‌ها'),
    ]

    report_type = models.CharField(max_length=50, choices=REPORT_TYPES,verbose_name='نوع گزارش')
    generated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reports',verbose_name='تولید شده توسط')
    generated_at = models.DateTimeField(auto_now_add=True,verbose_name='تولید شده در تاریخ')
    content = models.TextField(verbose_name='متن گزارش')

    def __str__(self):
        return f"Report {self.id} - {self.get_report_type_display()}"