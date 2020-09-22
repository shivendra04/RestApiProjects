from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username=request.GET.get('username')
        if username is None:
            return None
        try:
            user=User.objects.get(username=username)
        except:
            User.DoesNotExist
            raise AuthenticationFailed('Your credintials are invalid, plz provide valid credential to access end point')
        return (user,None)
class CustomAuthentication2(BaseAuthentication):
    def authenticate(self,request):
        username=request.GET.get('username')
        key=request.GET.get('key')
        if username is None or key is None:
            return None
        c1=len(key)==7
        c2=key[0]==username[-1].lower()
        c3=key[2]=='Z'
        c4=key[4]==username[0]
        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('Your username is invalid, plz provide valid credential to access end point')
        if c1 and c2 and c3 and c4:
            return (user,None)
        raise AuthenticationFailed('Your key is invalid, plz provide valid credential to access end point')
