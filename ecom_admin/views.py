from django.shortcuts import render,redirect
from customer.models import Customer
from reseller_app.models import Reseller
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def admin_home(request):
    seller_count = Reseller.objects.all().count()
    customer_count = Customer.objects.all().count()
    return render(request,'ecom_admin/admin_home.html',{'seller_count':seller_count,'customer_count':customer_count})
   

def approve_resellers(request):    
    reseller = Reseller.objects.filter(s_status = "pending")
    #reseller = Reseller.objects.all()
    return render(request,'ecom_admin/approve_resellers.html',{'pending':reseller})

def customers_list(request):
    return render(request,'ecom_admin/customers_list.html')

def registered_resellers(request):
    reseller = Reseller.objects.filter(s_status = "approved")
    return render(request,'ecom_admin/registered_resellers.html',{'pending':reseller})

def change_password(request):
    return render(request,'ecom_admin/change_password.html')

def admin_login(request):
    return render(request,'ecom_admin/adminlogin.html')

def r_approve(request,reseller_id):
    reseller= Reseller.objects.filter(id=reseller_id).update(s_status="approved")
    reseller1=Reseller.objects.get(id=reseller_id)
    subject = 'welcome to ecommerce  world'
    message = f'Hi {reseller1.s_name}, thank you for registering in ecommerce application.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['farhafinu36@gmail.com']
    send_mail( subject, message, email_from, recipient_list )
    return redirect('ecom_admin:approve_reseller')

def d_approve(request,reseller_id):
    reseller= Reseller.objects.get(id=reseller_id)
    reseller.delete()
    return render(request,'ecom_admin/registered_resellers.html')

# def testing(request):
#     return render(request,)    



