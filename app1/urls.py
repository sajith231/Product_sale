from django.urls import path
from .views import login_view,register_view,index,wishlist,wishlist_detail

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('index/', index, name='index'),
    path('wishlist/', wishlist, name='wishlist'),
     path('wishlist-detail/', wishlist_detail, name='wishlist_detail'),
]
