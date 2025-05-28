from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.contrib.auth.models import User
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import ProfileImageForm, UserUpdateForm
from django.contrib import messages
# Create your views here.

def landing_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'blog_app/landing.html')


def home(request):
    query = request.GET.get('q')

    if request.user.is_authenticated:
        post_list = BlogPost.objects.filter(author=request.user)

        if query:
            post_list = post_list.filter(
                Q(title__icontains = query) |
                Q(content__icontains = query)
            )
        post_list = post_list.order_by('-date_posted')
    else:
        post_list = BlogPost.objects.none()  # Show nothing when not logged in
    
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'blog_app/home.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog_app/post_detail.html', {'post':post})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)   # Don't save to DB yet
            post.author = request.user       # Set the author manually
            post.save()                      # Now save to DB
            
            return redirect('home')
    else:
        form = BlogPostForm()
    return render(request, 'blog_app/create_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = BlogPostForm(instance=post)  # ✅ This fills in the existing data

    return render(request, 'blog_app/edit_post.html', {'form': form, 'post': post})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'blog_app/delete_post.html', {'post': post})


from django.contrib.auth.forms import AuthenticationForm

def test_login_page(request):
    form = AuthenticationForm()
    return render(request, 'blog_app/login.html', {'form': form})

from django.contrib.auth import login
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            image = form.cleaned_data.get('image')
            if image:
                user.profile.image = image
                user.profile.save()
            login(request, user)  # Automatically logs in the user
            messages.success(request, "Account created successfully!")
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'blog_app/register.html', {'form': form})



@login_required
def profile(request):
    posts = BlogPost.objects.filter(author=request.user).order_by('-date_posted')

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        image_form = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and image_form.is_valid():
            user_form.save()
            image_form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        image_form = ProfileImageForm(instance=request.user.profile)

    return render(request, 'blog_app/profile.html', {
        'user_profile': request.user,
        'profile': request.user.profile,
        'posts': posts,
        'user_form': user_form,
        'image_form': image_form
    })



def public_profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = BlogPost.objects.filter(author=user).order_by('-date_posted')
    return render(request, 'blog_app/public_profile.html', {
        'user_profile': user,
        'profile': user.profile,
        'posts': posts
    })

def authors_list(request):
    authors = User.objects.all()
    return render(request, 'blog_app/authors.html', {'authors': authors})
