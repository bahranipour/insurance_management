from django.urls import path
from .views import (
    CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView,
    PolicyListView, PolicyCreateView, PolicyUpdateView, PolicyDeleteView,
    PaymentListView, PaymentCreateView, PaymentUpdateView, PaymentDeleteView,
    ClaimListView, ClaimCreateView, ClaimUpdateView, ClaimDeleteView,
    
)

urlpatterns = [
    # Customer URLs
    path('', CustomerListView.as_view(), name='customer-list'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer-create'),
    path('customers/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer-update'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),

    # Policy URLs
    path('policies/', PolicyListView.as_view(), name='policy-list'),
    path('policies/create/', PolicyCreateView.as_view(), name='policy-create'),
    path('policies/<int:pk>/update/', PolicyUpdateView.as_view(), name='policy-update'),
    path('policies/<int:pk>/delete/', PolicyDeleteView.as_view(), name='policy-delete'),

    # Payment URLs
    path('payments/', PaymentListView.as_view(), name='payment-list'),
    path('payments/create/', PaymentCreateView.as_view(), name='payment-create'),
    path('payments/<int:pk>/update/', PaymentUpdateView.as_view(), name='payment-update'),
    path('payments/<int:pk>/delete/', PaymentDeleteView.as_view(), name='payment-delete'),

    # Claim URLs
    path('claims/', ClaimListView.as_view(), name='claim-list'),
    path('claims/create/', ClaimCreateView.as_view(), name='claim-create'),
    path('claims/<int:pk>/update/', ClaimUpdateView.as_view(), name='claim-update'),
    path('claims/<int:pk>/delete/', ClaimDeleteView.as_view(), name='claim-delete'),

   
]