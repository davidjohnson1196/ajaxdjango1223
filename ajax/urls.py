from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('likepost/',views.likepost,name='likepost'),
    path('likecomment/',views.likecomment,name='likecomment'),
    path('likereply/',views.likecomment,name='likereply'),
]
