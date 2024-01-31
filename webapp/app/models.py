import requests
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
from rest_framework import serializers
from ckeditor.fields import RichTextField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify



class Contact(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(max_length=700, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    def __str__(self):
        return self.name



class FormContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Tên của bạn'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email của bạn'}),
            'message': forms.Textarea(attrs={'placeholder': 'Nội dung ....'}),
        }


# class AddProduct(forms.ModelForm):
#     # images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
#     class Meta:
#         model = Product
#         fields = ['name', 'category', 'price', 'price_sale', 'describe', 'digital', 'image', 'unit', 'count']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'describe': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 150px'}),
#             'price': forms.NumberInput(attrs={'class': 'form-control'}),
#             'price_sale': forms.NumberInput(attrs={'class': 'form-control'}),
#             'category': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input, d-flex'}),
#             'unit': forms.TextInput(attrs={'class': 'form-control'}),
#             'count': forms.NumberInput(attrs={'class': 'form-control'}),
#
#         }
#
# class AddCategory(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['sub_category', 'is_sub', 'name', 'slug', 'image']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'slug': forms.TextInput(attrs={'class': 'form-control'}),
#         }

# class AddSlide(forms.ModelForm):
#     class Meta:
#         model = Slide
#         fields = ['category_slide',  'name', 'status', 'image']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             # 'slug': forms.TextInput(attrs={'class': 'form-control'}),
#         }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ('username', 'email', 'first_name', 'last_name')






# // TRUYỆN
class Customer(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length =200,null=True)
    user_name = models.CharField(max_length =200,null=True)
    email = models.EmailField(max_length =200,null=True)
    password = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=10)
    birthdate = models.DateField()
    profile_image = models.ImageField(null=True, blank=True)

    @property
    def ImageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url
class Genre(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_genre', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True)
    slug = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name


class Story(models.Model):
    name = models.CharField(max_length=200, null=True)
    slug = models.CharField(max_length=200, null=True,blank=True)
    category = models.ManyToManyField(Genre, related_name='story_genre', blank=True)
    image = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=200, null=True)
    status = models.BooleanField(default=False, null=True, blank=False)
    description = models.TextField(null=True)
    view = models.IntegerField(default=0)
    count_comment = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    story_new = models.BooleanField(default=False, null=True, blank=False)

    # @receiver(pre_save, sender=Story.name)
    # def create_slug(sender, instance, **kwargs):
    #     if not instance.slug:
    #         instance.slug = slugify(instance.name)
    def __str__(self):
        return self.name
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Chapter(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='chapters')
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    date = models.DateField(default=timezone.now, null=True)
    view = models.IntegerField(default=0)
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    def __str__(self):
        return self.story.name + ' - ' + str(self.name)

class ImagesChapter(models.Model):
    chap = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.chap.story.name

class Comment(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    story = models.ForeignKey(Story, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.TextField(null=True, blank=False)
    date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    def __str__(self):
        return self.story
# Create your models here.
