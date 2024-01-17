"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from users import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('insertdata/',views.insertform),
    path('productdisplay/',views.displayproduct,name='return'),
    path('detailsview/<int:id>/',views.detailsview,name='display'),
    path('displayall/',views.displayall,name='home'),
    path('displayone/<int:id>/',views.displayone,name='single'),
    path('movie/',views.movieview,name='review'),
    path('register/',views.registerview,name='register'),
    path('login/',views.loginview,name='login'),
    path('logout/',views.logoutview,name='logout'),
    path('home/',views.homepageview,name='homepage')
    



]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)