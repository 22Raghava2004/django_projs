from django.shortcuts import render,get_object_or_404
from blog.models import Post

def allpost(request):
   from django.shortcuts import render
from blog.models import Post

def allpost(request):
    # Step 1: Get search term from the input box (GET method)
    search_term = request.GET.get('search')

    # Step 2: If something is searched, filter posts
    if search_term:
        posts = Post.objects.filter(title__icontains=search_term)
    else:
        posts = Post.objects.all()

    # Step 3: Send posts to the template
    return render(request, 'post.html', {'posts': posts})

def detail(request,blog_id):
    detail=get_object_or_404(Post,pk=blog_id)
    return render(request,'detail.html',{'post':detail})

# Create your views here.
