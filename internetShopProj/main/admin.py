from django.contrib import admin
from .models import *


admin.site.register([UserProfile, Category, Product, Review, Photo, Cart, CartItem])
