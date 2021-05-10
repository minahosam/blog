from django.shortcuts import render
from .models import post
from .forms import create_post_form
# Create your views here.
def all_posts(request):
    all=post.objects.all()
    if request.method == 'POST':
        create=create_post_form(request.POST)
        if create.is_valid():
            c=create.save(commit=False)
            c.author=request.user
            c.save()
    else:
        create=create_post_form()
    return render(request,'post/all_post.html',{'all':all, 'form':create})