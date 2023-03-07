from django.urls import path
from . import views

app_name = 'ecom_admin'

urlpatterns = [
    path('',views.admin_login,name='admin-login'),
    path('home',views.admin_home,name='admin_home'),
    path('approve-resellers',views.approve_resellers,name='approve_reseller'),
    path('customers-list',views.customers_list,name='list'),
    path('registered_resellers',views.registered_resellers,name='registered'),
    path('password_change',views.change_password,name='change-password'),
    path('r_approve/<int:reseller_id>',views.r_approve,name='r_approve'),
    path('d_approve/<int:reseller_id>',views.d_approve,name='d_approve'),
    
]