from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50,verbose_name='نام')
    last_name = models.CharField(max_length=50,verbose_name='نام خانوادگی')
    national_id = models.CharField(max_length=20, unique=True,verbose_name='کد ملی')
    phone_number = models.CharField(max_length=15,verbose_name='شماره تماس')
    email = models.EmailField(max_length=100, unique=True,verbose_name='ایمیل')
    address = models.TextField(verbose_name='آدرس')
    date_of_birth = models.DateField(verbose_name='تاریخ تولد')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='ایجاد شده')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Policy(models.Model):
    POLICY_TYPES = [
        ('health', 'سلامت'),
        ('auto', 'خودرو'),
        ('life', 'زندگی'),
        # سایر انواع بیمه‌نامه‌ها
    ]

    STATUS_CHOICES = [
        ('active', 'فعال'),
        ('inactive', 'غیرفعال'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='policies',verbose_name='نام و نام خانوادگی مشتری')
    policy_type = models.CharField(max_length=50, choices=POLICY_TYPES,verbose_name='نوع بیمه')
    start_date = models.DateField(verbose_name='تاریخ شروع')
    end_date = models.DateField(verbose_name='تاریخ پایان')
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2,verbose_name=' مبلغ حق بیمه')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active',verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='ایجاد شده')

    def __str__(self):
        return f"Policy {self.id} - {self.get_policy_type_display()}"
    

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('cash', 'نقدی'),
        ('card', 'کارت'),
        ('online', 'آنلاین'),
    ]

    STATUS_CHOICES = [
        ('success', 'موفق'),
        ('failed', 'ناموفق'),
    ]

    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name='payments',verbose_name='بیمه')
    payment_date = models.DateField(verbose_name='تاریخ پرداخت')
    amount = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='هزینه')
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS,verbose_name='روش پرداخت')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='success',verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='ایجاد شده')

    def __str__(self):
        return f"Payment {self.id} - {self.amount}"
    


class Claim(models.Model):
    STATUS_CHOICES = [
        ('pending', 'در حال بررسی'),
        ('approved', 'تایید شده'),
        ('rejected', 'رد شده'),
    ]

    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name='claims',verbose_name='بیمه')
    claim_date = models.DateField(verbose_name='تاریخ ادعا')
    claim_amount = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='هزینه ادعا')
    description = models.TextField(verbose_name='توضیحات')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending',verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='ایجاد شده')

    def __str__(self):
        return f"Claim {self.id} - {self.claim_amount}"