
from django.urls import path
from . import views

urlpatterns = [
   
    path('cart',views.cart,name='cart'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('min_cart/<int:product_id>/',views.min_cart,name='min_cart'),
    path('delete/<int:product_id>/',views.delete,name='delete'),

]