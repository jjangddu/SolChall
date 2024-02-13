from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.models import User
from .serializers import UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def getUser(request):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postUser(request):
    user = UserSerializer(data=request.data)
    if user.is_valid():
        user.save()
        return Response(user.data)
    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({'error':{
            'code': 404,
            'message': 'User not found'
        }}, status=status.HTTP_404_NOT_FOUND)

    # Note: This block should be outside the 'except' block
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#전체 삭제
@api_view(['DELETE'])
def delete(request):
    query = User.objects.all()
    query.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#id별 삭제하기
@api_view(['DELETE'])
def deleteById(request, id):
    try:
        query = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({'error':{
            'code' : 404,
            'message' : 'User not found'
        }}, status = status.HTTP_404_NOT_FOUND)
    query.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



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
