from datetime import datetime
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

#recipe post
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField()
    premium = models.BooleanField(default=False)
    image = models.ImageField(blank=True, upload_to='recipe_images')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='recipe_posts')
    def __str__(self):
        return self.title
    
class NavigationMenu(models.Model):
    title = models.CharField(max_length=50)
    link  = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    
class SocialMedia(models.Model):
    title = models.CharField(max_length=50)
    link  = models.CharField(max_length=200)
    icons = models.CharField(max_length=150)
    disable = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Contact(models.Model):
    address = models.TextField()
    phone = models.BigIntegerField()
    email = models.CharField(max_length=200)
    support = models.CharField(max_length=200)
    location = models.CharField(max_length=200,blank=True)
    hours = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.email

class BannerManegment(models.Model):
    title = models.CharField(max_length=50)
    banner_image = models.ImageField(blank=True, upload_to="banner")
    status = models.BooleanField(default=True)
    navigationid = models.OneToOneField(NavigationMenu, verbose_name="Navigation ID", on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class ProfileSettings(models.Model):
    phone = models.BigIntegerField(max_length=20)
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name="User Name")
    user_photo = models.ImageField(upload_to="userimages",verbose_name="User Picture")
    bio = models.TextField(verbose_name="User Bio Data")
    def __str__(self):
        return self.user.username
class Subscribe(models.Model):
    status = models.BooleanField(default=True,verbose_name="Disable")
    email = models.CharField(max_length=100,verbose_name="Subscribe Email")
    def __str__(self):
        return self.email

class Ads(models.Model):
    ads_link =models.CharField(max_length=200,verbose_name="Ads Link")
    ads_created = models.DateTimeField(default=datetime.now(),verbose_name="Ads Created Date")
    status = models.BooleanField(default=False,verbose_name="Disable")
    ads_title = models.CharField(max_length=200,verbose_name="Ads Title")
    ads_image = models.ImageField(verbose_name="Ads Image",upload_to="ads")
    def __str__(self):
        return self.ads_title

class Bloginfo(models.Model):
    blog_title = models.CharField(max_length=150,verbose_name="title")
    blog_icon  = models.CharField(max_length=100,verbose_name="icon")
    blog_description = models.TextField(verbose_name="blog description")
    def __str__(self):
        return self.blog_title

class FooterMenu(models.Model):
    menu_title = models.CharField(max_length=100,verbose_name="title")
    menu_link = models.CharField(max_length=100,verbose_name="link")
    menu_status = models.BooleanField(default=False,verbose_name="Disable")
    def __str__(self):
        return self.menu_title

class Enquiry(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    message = models.TextField()
    def __str__(self):
        return self.subject
    
    
    
    
    