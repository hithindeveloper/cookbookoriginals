from django.urls import path
from . import views
app_name="frontend"
urlpatterns = [
    path('',views.index,name="home"),
    path("singlepage/<int:id>",views.singlepage,name="singlepage"),
    path("category/<str:category>",views.category,name="category"),
    path("aboutus",views.aboutus,name="aboutus"),
    path("search",views.search,name="search"),
    path("subscribe",views.subscribe,name="subscribe"),
    path("contact",views.contact,name="contact"),
    path("addquery",views.addquery,name="addquery"),
    path("recipies",views.recipies,name="recipies"),
    path("sendemail",views.sendemail,name="sendemail"),
]