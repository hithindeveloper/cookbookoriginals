from django.contrib import admin
from .models import *
from django.contrib.auth.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Register your models here.
admin.site.register(Recipe)
admin.site.register(NavigationMenu)
admin.site.register(SocialMedia)
admin.site.register(Contact)
admin.site.register(BannerManegment)
admin.site.register(ProfileSettings)
admin.site.register(Subscribe)
admin.site.register(Ads)
admin.site.register(Bloginfo)
admin.site.register(FooterMenu)
admin.site.register(Enquiry)