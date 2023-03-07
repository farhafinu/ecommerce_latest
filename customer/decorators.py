from django.shortcuts import render, redirect

def auth_customer(func):
    def wrap(request, *args, **kwargs):
        if 'c_id' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('customer:home')
    return wrap