from django.urls import path
from . import views

app_name = 'reseller'

urlpatterns = [
    path('',views.reseller_home, name='reseller_home'),
    path('p-catalogue',views.product_catalogue, name='catalogue'),
    path('update-stock',views.update_stock, name='update_stock'),
    path('product-add',views.add_product, name='add_product'),
    path('my-order',views.my_order, name='reseller_orders'),
    path('recent-orders',views.recent_orders, name='recent_orders'),
    path('cancelled-order',views.cancelled_orders, name='cancelled_order'),
    path('history_order',views.order_history, name='order_history'),
    path('password-change',views.change_password, name='change_password'),
    path('sellerac',views.seller_ac, name='seller-acnt'),
    path('editprofile',views.edit_profile, name='edit_profile'),
    path('seller_logot',views.seller_logout, name='seller_logout'),
    path('get_product',views.get_product, name='get_product'),
    path('get_stock',views.get_stock, name='get_stock'),
    path('change_password',views.change_password,name='change_password'),
    
]