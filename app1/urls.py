from django.urls import path
from .views import login_view,register_view,index,wishlist

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('index/', index, name='index'),
    path('wishlist/', wishlist, name='wishlist'),
]
