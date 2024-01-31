# from itertools import product
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import *


# app
from .python.app.base import *
from .python.app.information_address import information_address
from .python.app.cart import cart
from .python.app.blog import blog
from .python.app.shop import shop
from .python.app.category import category
from .python.app.check_address import Continue1
from .python.app.checkout import checkout
from .python.app.detail import detail
from .python.app.information import Information, edit_information
from .python.app.login import loginPage, logoutPage
from .python.app.register import register
from .python.app.search import searchProduct
from .python.app.updateItem import updateItem
from .python.app.contact import contact
from .python.app.manage_address import addAddress, editAddress, deleteAddress
from .python.app.my_order import myOrder, deletemyOrder


# admin
from .python.admin.manage import Manage
from .python.admin.home_manage import homeManage
from .python.admin.manage_slide import manageSlide, addSlide, editSlide, deleteSlide, get_slide
from .python.admin.updateStatus import update_status
from .python.admin.manage_user import manageUser, deleteUser, addUser, editUser
from .python.admin.managr_order import manageOrder, viewOrder, delOrder
from .python.admin.manage_category import manageCategory, addCategory, editCategory, deleteCategory
from .python.admin.manage_product import manageProduct, addProduct, editProduct, deleteProduct, viewProduct


#API

from .API.products_api import *


import hashlib
import hmac
import json
import urllib
import urllib.parse
import urllib.request
import random
import requests
from datetime import datetime
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
# from django.utils.http import urlquote



from django.urls import reverse
from django.shortcuts import render
