from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import User


# Create your views here.

def signup_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password_confirm = request.POST.get('password_confirm', None)

        if password != password_confirm:
            return render(request, 'user/signup.html')
        else:
            exist_user = User.objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html')
            else:
                new_user = User(username=username, password=password)
                new_user.save()
                return redirect('/signin')


def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = User.objects.get(username=username)
        if me.password == password:
            request.session['username'] = me.username
            return HttpResponse(f'로그인 성공! {me.username}님 환영합니다!')
        else:
            return redirect('/signin')

    elif request.method == 'GET':
        return render(request, 'user/signin.html')
