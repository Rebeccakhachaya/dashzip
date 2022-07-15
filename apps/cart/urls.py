from django.urls import path
from . import views
urlpatterns = [
    # path('display', views.orders, name = 'users'),
    path('order/<str:id>',views.single_order,name='order'),
 ]