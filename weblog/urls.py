from django.contrib import admin
from django.urls import path, include
from . import views
from register import views as v


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('weblogapp.urls')),
    path("register/", v.register, name="register"),
    ]