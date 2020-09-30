from django.shortcuts import render
from .models import Post,Like
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.
def home(request):
    posts=Post.objects.all()
    print(posts)
    return render(request,'ajax/home.html',{'posts':posts})

def likepost(request):
    if request.method=="GET":
        post_id=request.GET['post_id']
        user=request.GET['user']
        #allresponses=[]
        #campcreated=Like.objects.values('post','id')
        #print(campcreated)
        #cats={item['post'] for item in campcreated}
        #print(cats)
        #for cat in cats:
         #   likes=Like.objects.filter(post=cat)
          #  allresponses.append(likes)
        likedpost=Post.objects.get(id=post_id)
        userliked=User.objects.get(id=user)
        m=Like(post=likedpost,likedby=userliked)
        m.save()
        #print(allresponses)
        #params = {'allresponses': allresponses}
        return HttpResponse("Your response has been noted. Thank You ")
    else:
        return HttpResponse("request method isnot Get!!")

