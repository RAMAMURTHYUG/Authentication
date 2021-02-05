from django.contrib import admin
from django.urls import path,include
from authapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('java/',views.java),
    path('python/',views.python),
    path('apti/',views.apti),
    path('logout/',views.logout),
    path('accounts/',include("django.contrib.auth.urls")),
    path('signup/',views.Signup),
]
