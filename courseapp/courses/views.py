from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.

def get_Sign(request):
    return render(request,'Sign.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # hoặc bất kỳ view nào bạn muốn chuyển hướng đến
        else:
            # Xử lý đăng nhập thất bại
            pass
    return render(request, 'Sign.html')
