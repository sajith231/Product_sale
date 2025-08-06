from django.urls import path
from .views import login_view,register_view,index,wishlist,wishlist_detail,my_chats,add_product_page,select_category_page

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('index/', index, name='index'),
    path('wishlist/', wishlist, name='wishlist'),
    path('wishlist-detail/', wishlist_detail, name='wishlist_detail'),
    path('my-chats/', my_chats, name='my_chats'),

    
    path('select-category/', select_category_page, name='select_category'),
    path('add-product-details/', add_product_page, name='add_product_details'),

]
