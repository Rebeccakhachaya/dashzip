from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

# def orders(request):
#     #pull data from third party rest api
#     # https://jsonplaceholder.typicode.com/users
#     response = requests.get('https://jsonplaceholder.typicode.com/users')
#     #convert reponse data into json
#     users = response.json()
#     #print(users)
#     return render(request, "users.html", {'users': users})
#     pass


def get_order(request):
   response = requests.get('https://django.fulusi.org/api/v1/gas_orders?page=1',headers={'Authorization':'Fulusi a9f58720df564306183c5035da0e847ea1e29e62'})
   data = response.json()
   id=data["results"]
   # data = response.json().results
   # print(response.json())
   print(id)

   return render(request,'get_orders.html',{'response':id})

