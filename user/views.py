from .serializer import UserSerializer, RegisterSerializer
from .models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny 
from .permissions import IsThisMine, Master # custom permissions



@api_view(['GET'])
@permission_classes([Master])
def user_home(request, *args, **kwargs):
    qs = User.objects.all()
    data = UserSerializer(qs, many=True).data
    return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def registration(request, *args, **kwargs):
    input = request.data
    data = {
        "email": input.get('email'),
        "first_name": input.get('first_name'),
        "last_name": input.get('last_name'),
        "user_role": input.get('user_role'),
        "company": input.get('company'),
        "designation": input.get('designation'),
        "password": input.get('password'),
    }
    serializer = RegisterSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        UserSerializer(user)
        return Response("Account Successfully Created!")

    
@api_view(['GET'])
@permission_classes([IsThisMine])
def detail(request, *args, **kwargs):
    input = request.data
    email = input.get('email')
    item = User.objects.get(email=email)
    data = UserSerializer(item, many=False).data
    return Response(data)


@api_view(['POST','PATCH'])
@permission_classes([IsThisMine])
def update(request, *args, **kwargs):
    input = request.data
    email = input.get('account')
    item = User.objects.get(email=email)
    serializer = UserSerializer(item, data=input, partial=True)
    if "password" in input:
        item.set_password(input['password'])
        item.save()

    if "user_role" in input:
        if input["user_role"] == "ADMIN": # give permission of superuser
            item.is_superuser = True

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET','DELETE'])
@permission_classes([IsThisMine])
def delete(request, *args, **kwargs):
    input = request.data
    email = input.get('email')
    item = User.objects.get(email=email)
    item.delete()
    return Response('Account Successfully Deleted')
