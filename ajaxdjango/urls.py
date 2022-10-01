from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('ajax.urls')),
    path('home/',views.home),
    path('about/',views.about,name=about),
]
