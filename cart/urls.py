from django.urls import path
from .views import  cart_detail, cart_add_one_product, cart_add, cart_remove, cart_update

app_name = 'cart'

urlpatterns = [
   path('', cart_detail, name='cart_detail'),
   # path('checkout', CheckoutView.as_view(), name='CheckoutView'),
   path('add/<int:product_id>/', cart_add, name='cart_add'),
   path('ajouter-au-panier', cart_add_one_product, name='cart_add_one_product'),
   path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
   path('update/<int:product_id>/', cart_update, name='cart_update'),

]

