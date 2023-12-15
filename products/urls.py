from django.urls import path
from . import views as product_views

urlpatterns = [
    path('', product_views.store,name='store'),
    path('cart/', product_views.cart,name='cart'),
    path('checkout/', product_views.checkout,name='checkout'),
    path('update_item/', product_views.updateItem,name='update_item'),
    
]