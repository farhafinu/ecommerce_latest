 
from itertools import product
from urllib import request
from django.shortcuts import render,redirect
from . decorators import auth_customer
from customer.models import AddCart, Customer, Order, Order_detail
from reseller_app.models import Product, Reseller
from django.db.models import F,Sum
from django.http import JsonResponse
import razorpay
from django.conf import settings


# Create your views here.

def customer_home(request):
    msg = ""
    if request.method =='GET':

        status = False
    if request.method == 'POST':
        if 'c_signup' in request.POST:
            first_name = request.POST['fname']
            second_name = request.POST['sname']
            e_mail = request.POST['c_email']
            c_phone = request.POST['c_phno']
            c_password = request.POST['c_passwd']
            c_address = request.POST['c_addrs']
            email_exists = Customer.objects.filter(email = e_mail).exists()
            if not email_exists:
                customer = Customer(
                    first_name = first_name,
                    last_name =second_name,
                    email = e_mail,
                    mobile = c_phone,
                    password = c_password,
                    address = c_address)
                customer.save()
            else:
                msg="email already exists"      
            

        if 'c_login' in request.POST:
            email = request.POST['c_user_id']
            passwd = request.POST['c_user_passwd']

            try:
                customer = Customer.objects.get(email = email,password = passwd)
                request.session['c_id'] = customer.id
                
                 
            except:
                error_msg = 'Invalid Username Or Password'
                return render(request,'customer/customer_home.html',{'error_msg':error_msg})#customer end
     
   
        if 's_signup' in request.POST:
            s_name = request.POST['s_name']
            s_email = request.POST['s_email']
            s_mobile = request.POST['s_mobile']
            s_address = request.POST['s_address']
            s_account = request.POST['s_account']
            s_ifsc = request.POST['s_ifsc']
            s_acholder = request.POST['s_acholder']
            s_password = request.POST['s_password']
            seller_pic = request.FILES['pic']
            email_exists = Reseller.objects.filter(email = s_email).exists()
            # if not email_exists:

            reseller = Reseller(s_name = s_name,email = s_email,mobile = s_mobile,address = s_address,account_no =s_account,ifsc = s_ifsc,
            s_acholdername = s_acholder,password = s_password,s_pic = seller_pic)
            reseller.save()
            # else:
            #     msg="email already exists"              

        if 'signin' in request.POST:

            email = request.POST['s_mail']
            passwd = request.POST['s_pass']
            print('seller')

            try:
                reseller = Reseller.objects.get(email = email,password = passwd)
                if reseller.s_status == "approved":
                    request.session['s_id'] = reseller.id               
                    return redirect("reseller:reseller_home")
                else:
                    error_msg = "your account not verified"
            except:
                error_msg = 'Invalid Username Or Password'
                return render(request,'customer/customer_home.html',{'error_msg':error_msg}) 
                   
    latest_product_list = Product.objects.all()
    return render(request,'customer/customer_home.html',{'products':latest_product_list,'error_msg':msg})
    

@auth_customer
def my_cart(request):
    
    return redirect('customer:view_cart') 

@auth_customer
def view_cart(request):    
    cart2=AddCart.objects.annotate(total_price = F('product__p_price') * F('qty'))
    sum=0
    for i in cart2:
        sum=sum+i.total_price
    
    #gt=AddCart.objects.aaggregate(grt =Sum( F('product__p_price') * F('qty')))
    #gt=cart2.aaggregate(grt=Sum(F('total_price')))   
    request.session['gt']=sum
    return render(request,'customer/my_cart.html',{'cart_items':cart2,'gt':sum})
    
@auth_customer
def del_cart_item(reqest,product_id):
    del_item=AddCart.objects.filter(product_id=product_id,customer_id=reqest.session['c_id'])
    del_item.delete()
    return redirect('customer:view_cart') 

@auth_customer
def my_order(request):

    orders=Order_detail.objects.filter(customer_id=request.session['c_id'])
    return render(request,'customer/my_orders.html',{'orders':orders})
 
def product_detail(request,product_id):
    product_detail=Product.objects.get(id=product_id)
    if request.method == "POST":
        p_id=request.POST['pid']
        p_qty=request.POST['qty'] 
        
        

        if 'c_id' not in request.session: 
            msg="please login"    
            return render(request,'customer/product_detail.html',{'product':product_detail,'error':msg})
        else:  
            product_exist=AddCart.objects.filter(product_id=p_id, customer = request.session['c_id']).exists()
            if not product_exist:
                cart = AddCart(
                product_id = p_id ,
                qty=p_qty,
                customer_id = request.session['c_id'])
                cart.save()
            
        return redirect('customer:view_cart')


    
    return render(request,'customer/product_detail.html',{'product':product_detail})

@auth_customer
def my_ac(request):
    customer_P=Customer.objects.get(id=request.session['c_id']) #select * from table where     
    return render(request,'customer/my_account.html',{'customer_details':customer_P})
    
@auth_customer
def editprofile(request):
  
         
    customer_P=Customer.objects.get(id=request.session['c_id'])
    if request.method == 'POST':
        customer_edit = Customer.objects.get(id = request.session['c_id'])
        customer_edit.first_name = request.POST['first-name']
        customer_edit.last_name = request.POST['last-name']
        customer_edit.email = request.POST['email']
        customer_edit.mobile = request.POST['mobile']
        customer_edit.address = request.POST['address']
        customer_edit.save()
        return redirect('customer:my-account')


    customer_edit1 = Customer.objects.get(id = request.session['c_id'])
    return render(request,'customer/editform.html',{'edit_profile':customer_edit1,'customer_details':customer_P})

    

@auth_customer
def select_address(request):
   
    customer_address=Customer.objects.get(id=request.session['c_id']) #select * from table where

    return render(request,'customer/address.html',{'customer_address':customer_address})

@auth_customer
def c_payment(request):
    name=Customer.objects.get(id=request.session['c_id']).first_name
    amount=request.session['gt']
    return render(request,'customer/payment.html',{'nmae':name,'amount':amount})

def c_logout(request):
    del request.session['c_id']
    request.session.flush()
    return redirect('customer:home')

def email_exist(request):
    email = request.POST['email']

    e_exists = Customer.objects.filter(email = email).exists()
    
    return JsonResponse({'status':e_exists})


def change_qty(request):

    quatity = int(request.POST['quantity'])
    p_id = request.POST['p_id']
    
    stock = Product.objects.get(id=p_id)
    print(stock.p_stock)
    print(quatity,p_id)
    
    if stock.p_stock > quatity:
        changeqty = AddCart.objects.get(product_id=p_id)
        print (changeqty.qty)
        changeqty.qty=quatity
        changeqty.save()
        status=True
        cart2=AddCart.objects.annotate(total_price = F('product__p_price') * F('qty'))
        sum=0
        for i in cart2:
            sum=sum+i.total_price
        msg="qty update successfully"
    
        return JsonResponse({'data':sum ,'status':status})
    else:
        status=False
        return JsonResponse({'status':status})

def order_payment(request):
    if request.method == "POST":
        c_id = request.session['c_id']
        amount = request.POST['total']
        order_recipt="order_reciptid_11"
        notes={'shipping address':'bomalahalli,bangolre'}

        products= Order.objects.filter(customer_id=request.session['c_id'],status='pending')

        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        payment = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1",'notes':notes}
        )

        
        print(payment)
        return JsonResponse(payment)


        # order = Order.objects.create(
        #     name=name, amount=amount, provider_order_id=payment_order["id"]
        # )
        # order.save()
        # return render(
        #     request,
        #     "payment.html",
        #     {
        #         "callback_url": "http://" + "127.0.0.1:8000" + "/razorpay/callback/",
        #         "razorpay_key":settings.RAZORPAY_KEY_ID,
        #         "order": order,
        #     },
        # )
        
def updatepayment(request):
    user_id=request.session['c_id']
    Order.objects.filter(id=request.session['oid'],customer_id=user_id, status='pending').update(status="paid")
    pid=Order.objects.filter(id=request.session['oid'],customer_id=user_id, status='pending')
    customer_id=request.session['c_id']
    products=AddCart.objects.filter(customer_id=customer_id) 

    for pro in products:

        print(pro.product_id)

        order=Order_detail(customer_id=customer_id,
                    productid_id=pro.product_id,
                    price=pro.product.p_price,
                    quantity=pro.qty,
                    status="paid",
                    payment_type="Razorpay",
                    order_id= pid.id
        )
        order.save()
        products.delete()

    Order_detail.objects.filter(customer_id=user_id, status='order_pending',order_id=request.session['oid']).update(status='paid')
    return JsonResponse({'resp':'sucsses'})


def checkout(request):
    customer_id=request.session['c_id']

    od=Order(customer_id=customer_id,amount=request.session['gt'],status='pending')
    od.save()
    request.session['oid']= od.id
    products=AddCart.objects.filter(customer_id=customer_id) 


    for pro in products:

        print(pro.product_id)

        order=Order_detail(customer_id=customer_id,
                    productid_id=pro.product_id,
                    price=pro.product.p_price,
                    quantity=pro.qty,
                    status="order_pending",
                    payment_type="Razorpay",
                    order_id=od.id        
                    )
        order.save()
    products.delete()

    name=Customer.objects.get(id=request.session['c_id']).first_name
    amount=request.session['gt']
    return render(request,'customer/payment.html',{'nmae':name,'amount':amount})  

def update(request):
    user_id=request.session['c_id']
    Order.objects.filter(id=request.session['oid'],customer_id=user_id, status='pending').update(status="paid")

    Order_detail.objects.filter(customer_id=user_id, status='order_pending',order_id=request.session['oid']).update(status='paid')

    orders=Order_detail.objects.filter(customer_id=request.session['c_id'])

    return render(request,'customer/my_orders.html',{'orders':orders})

def change_password(request):
    if request.method == 'POST':
        change_password = Customer.objects.get(id = request.session['c_id'])
        change_password.password = request.POST['new_pass']
        change_password.save()
        return redirect('customer:home')
    change_password1 = Customer.objects.get(id = request.session['c_id'])
    return render(request,'customer/change_password.html',{'change_password':change_password1})

