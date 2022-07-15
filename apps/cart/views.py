from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.


def single_order(request,*args,**kwargs ):
   response = requests.get(f"https://django.fulusi.org/api/v1/get_order/{kwargs['id']}",headers={'Authorization':'Fulusi a9f58720df564306183c5035da0e847ea1e29e62'})
   response_body = response.json()
   results = response_body["results"]
   data=results["data"]
   delivery_location=data["deliveryLocation"]
   shopping_cart=data["orders"]
   
   print(shopping_cart)
   
#    id=data["results"]
#    print(response.json())
#    print(id)

   return render(request,'order.html',{'data':data})
