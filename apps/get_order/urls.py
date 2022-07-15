from django.urls import path
from . import views
urlpatterns = [
    # path('display', views.orders, name = 'users'),
    path('display',views.get_order,name='get_order'),
 ]