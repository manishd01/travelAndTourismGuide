"""travelAndTourism URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *
from location.views import *
from about.views import *
from contactus.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage),
    # path('login/',login),
    path('signin/signin/loggedin/',login),
    path('signin/loggedin/',login),
    path('signup/addNewUser/signin/',login),
    path('signin/',sign_in),
    path('signup/',sign_up),
    # path('signup/add_new_user/',sign_up),
    path('location/',location),
    # path('basic',basic),
    path('about/',about),
    path('contact_us/',contactus),
    path('location/kangra/',kangra),
    path('location/una/',una),
    path('location/kullu/',kullu),
    path('location/chamba/',chamba),
    path('location/solan/',solan),
    path('location/sirmaur/',sirmaur),
    path('location/hamirpur/',hamirpur),
    path('location/kinnaur/',kinnaur),
    path('location/bilaspur/',bilaspur),
    path('location/lahul_spiti/',lahul_spiti),
    path('location/shimla/',shimla),
    path('location/mandi/',mandi),
    # path('addNewUser/',add_user),
    path('signup/addNewUser/',add_user) #if this line missing , we get an error


]
