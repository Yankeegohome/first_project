from django.urls import path
from .views import *


urlpatterns = [
    path('', test, name='test'),
    path('product/<int:pk>', get_product, name='product'),
]