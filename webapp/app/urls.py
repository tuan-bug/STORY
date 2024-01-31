from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
    path('base/', views.base, name="base"),
    path('', views.getHome, name="home"),
    path('shop/', views.shop, name="shop"),
    path('blog/', views.blog, name="blog"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutPage, name="logout"),
    path('search/', views.searchProduct, name="search"),
    path('category/', views.category, name="category"),

    path('detail/', views.detail, name="detail"),
    path('chapter_detail/<slug:chapter_slug>/', views.detail_chapter, name='chapter_detail'),


    path('address/', views.Continue1, name="address"),
    path('information/', views.Information, name="information"),
    path('edit_information/', views.edit_information, name="edit_information"),
    path('contact/', views.contact, name="contact"),
    path('information_address/', views.information_address, name="information_address"),
    path('deleteAddress/', views.deleteAddress, name="deleteAddress"),
    path('addAddress/', views.addAddress, name="addAddress"),
    path('editAddress/', views.editAddress, name="editAddress"),
    path('my_order/', views.myOrder, name="myOrder"),
    path('delete_my_order/', views.deletemyOrder, name="delete_myOrder"),

    # ADMIN
    path('manage/', views.Manage, name="manage"),
    path('home_manage/', views.homeManage, name="home_manage"),
    path('manageSlide/', views.manageSlide, name="manageSlide"),
    path('addSlide/', views.addSlide, name="addSlide"),
    path('get_slide/<int:slide_id>/', get_slide, name='get_slide'),
    path('editSlide/<int:slide_id>/', views.editSlide, name="editSlide"),
    # path('editStatus/', views.editStatus, name="editStatus"),
    path('deleteSlide/<int:id>', views.deleteSlide, name="deleteSlide"),
    path('update_status/', views.update_status, name="update_status"),
    #PRODUCTS
    path('manageProduct/', views.manageProduct, name="manageProduct"),
    path('addProduct/', views.addProduct, name="addProduct"),
    path('editProduct/', views.editProduct, name="editProduct"),
    path('deleteProduct/<int:id>', views.deleteProduct, name="deleteProduct"),
    path('viewProduct/', views.viewProduct, name="viewProduct"),

    #CATEGORY
    path('manageCategory/', views.manageCategory, name="manageCategory"),
    path('addCategory/', views.addCategory, name="addCategory"),
    path('editCategory/', views.editCategory, name="editCategory"),
    path('deleteCategory/<int:id>', views.deleteCategory, name="deleteCategory"),

    #ORDER
    path('manageUser/', views.manageUser, name="manageUser"),
    path('addUser/', views.addUser, name="addUser"),
    path('editUser/', views.editUser, name="editUser"),
    path('delUser/<int:id>', views.deleteUser, name="deleteUser"),


    path('manageOrder/', views.manageOrder, name="manageOrder"),
    path('viewOrder/', views.viewOrder, name="viewOrder"),
    path('delOrder/<int:id>', views.delOrder, name="deleteOrder"),








]
