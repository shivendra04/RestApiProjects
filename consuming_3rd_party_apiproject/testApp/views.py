from django.shortcuts import render
import requests

# Create your views here.
def get_geographic_info(request):
    ip=request.META.get('HTTP_X_FORWARDED_FOR',"") or request.META.get('REMOTE_ADDR')
    #url='http://api.ipstack.com/'+str(ip)+'?access_key=9ffb2b8b37c1aa0ea5bb7f5f6fd44683'
    url='http://api.ipstack.com/47.9.1.116?access_key=9ffb2b8b37c1aa0ea5bb7f5f6fd44683'
    response=requests.get(url)
    data=response.json()
    return render(request,'testApp/info.html',data)
