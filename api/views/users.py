from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from ..serializers.user import UserSerializer
from django.contrib.auth import authenticate,login,logout


class SignUp(generics.CreateAPIView):
    #Overriding the default authentication and permissions classes to be None 
    authentication_classes = ()
    permission_classes = ()

    def post(self,request):
        new_user = UserSerializer(data=request.data)
        if new_user.is_valid():
            new_user.save()
            return Response({'user': new_user.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({new_user.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class SignIn(generics.CreateAPIView):
     #Overriding the default authentication and permissions classes to be None 
    authentication_classes = ()
    permission_classes = ()

    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request,user)

            #Delete token if one is present and generate a new one
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            user.token = token.key
            user.save()
            return Response({
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'token': token.key
                }
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({'msg': 'The username and/or password is incorrect'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class SignOut(generics.DestroyAPIView):
    def delete(self,request):
        user = request.user

        #Remove all tokens for the user
        Token.objects.filter(user=user).delete()
        user.token = None
        #Save tokenless user to database 
        user.save()
        #Logout to remove all session data
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

class PasswordChange(generics.CreateAPIView):
    def put(self,request):
        old = request.data['passwords']['old']
        user = request.data
        if user.check_password(old):
            user.set_password(request.data['passwords']['new'])
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)