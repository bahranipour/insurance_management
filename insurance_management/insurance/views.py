from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Customer,Policy,Payment,Claim
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomerListView(LoginRequiredMixin,ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers'
    paginate_by = 10

class CustomerCreateView(LoginRequiredMixin,CreateView):
    model = Customer
    template_name = 'customers/customer_form.html'
    fields = ['first_name', 'last_name', 'national_id', 'phone_number', 'email', 'address', 'date_of_birth']
    success_url = reverse_lazy('customer-list')

class CustomerUpdateView(LoginRequiredMixin,UpdateView):
    model = Customer
    template_name = 'customers/customer_form.html'
    fields = ['first_name', 'last_name', 'national_id', 'phone_number', 'email', 'address', 'date_of_birth']
    success_url = reverse_lazy('customer-list')

class CustomerDeleteView(LoginRequiredMixin,DeleteView):
    model = Customer
    template_name = 'customers/customer_confirm_delete.html'
    success_url = reverse_lazy('customer-list')





class PolicyListView(LoginRequiredMixin,ListView):
    model = Policy
    template_name = 'policies/policy_list.html'
    context_object_name = 'policies'
    paginate_by = 10

class PolicyCreateView(LoginRequiredMixin,CreateView):
    model = Policy
    template_name = 'policies/policy_form.html'
    fields = ['customer', 'policy_type', 'start_date', 'end_date', 'premium_amount', 'status']
    success_url = reverse_lazy('policy-list')

class PolicyUpdateView(LoginRequiredMixin,UpdateView):
    model = Policy
    template_name = 'policies/policy_form.html'
    fields = ['customer', 'policy_type', 'start_date', 'end_date', 'premium_amount', 'status']
    success_url = reverse_lazy('policy-list')

class PolicyDeleteView(LoginRequiredMixin,DeleteView):
    model = Policy
    template_name = 'policies/policy_confirm_delete.html'
    success_url = reverse_lazy('policy-list')





class PaymentListView(LoginRequiredMixin,ListView):
    model = Payment
    template_name = 'payments/payment_list.html'
    context_object_name = 'payments'
    paginate_by = 10

class PaymentCreateView(LoginRequiredMixin,CreateView):
    model = Payment
    template_name = 'payments/payment_form.html'
    fields = ['policy', 'payment_date', 'amount', 'payment_method', 'status']
    success_url = reverse_lazy('payment-list')

class PaymentUpdateView(LoginRequiredMixin,UpdateView):
    model = Payment
    template_name = 'payments/payment_form.html'
    fields = ['policy', 'payment_date', 'amount', 'payment_method', 'status']
    success_url = reverse_lazy('payment-list')

class PaymentDeleteView(LoginRequiredMixin,DeleteView):
    model = Payment
    template_name = 'payments/payment_confirm_delete.html'
    success_url = reverse_lazy('payment-list')





class ClaimListView(LoginRequiredMixin,ListView):
    model = Claim
    template_name = 'claims/claim_list.html'
    context_object_name = 'claims'
    paginate_by = 10

class ClaimCreateView(LoginRequiredMixin,CreateView):
    model = Claim
    template_name = 'claims/claim_form.html'
    fields = ['policy', 'claim_date', 'claim_amount', 'description', 'status']
    success_url = reverse_lazy('claim-list')

class ClaimUpdateView(LoginRequiredMixin,UpdateView):
    model = Claim
    template_name = 'claims/claim_form.html'
    fields = ['policy', 'claim_date', 'claim_amount', 'description', 'status']
    success_url = reverse_lazy('claim-list')

class ClaimDeleteView(LoginRequiredMixin,DeleteView):
    model = Claim
    template_name = 'claims/claim_confirm_delete.html'
    success_url = reverse_lazy('claim-list')