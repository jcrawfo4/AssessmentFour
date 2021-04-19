from django.shortcuts import render, redirect
from . models import Category, Post
from .forms import CategoryForm, PostForm

# Create your views here.

def categories(request):
    all_categories = Category.objects.all()
    return render(request, 'categories.html', {'all_categories':all_categories})

def get_category(category_id):
    return Category.objects.get(id=category_id)

def category_details(request, category_id):
    category_detail= get_category(category_id)
    category_post = category_detail.posts.all()
    return render(request, 'category_detail.html', {'category': category_detail, 'posts':category_post})

def new_category(request):
    if request.method== "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', 
            category_id = category.id)
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form':form, 'type':'New'})

def category_edit(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            #category.author = User.objects.first()
            #category.published_date = datetime.datetime.now()
            category.save()
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form, 'type': 'Edit'})

def category_delete(request, category_id):
    if request== 'POST':
        category = Category.objects.get(id=category_id)
        category.delete()
    return redirect('categories')

##### posts
def post_detail(request, category_id, post_id):
    category = Category.objects.get(id = category_id)
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'category': category, 'post': post})

def new_post(request, category_id):
    category = get_category(category_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print("this happened !!!!")
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', category_id=category.id, post_id=post.id)
        else: 
            print(form.errors)
            return render(request, 'post_form.html', {'form':form, 'type':'New', 'category':category})
    else:
        form = PostForm(initial={'category':category})
    return render(request, 'post_form.html', {'form':form, 'type':'New', 'category':category})

def post_edit(request, category_id, post_id):
    post = Post.objects.get(id=post_id)
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', category_id=post.category.id, post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form, 'type': 'Edit', 'category':category})


def post_delete(request, category_id, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        post.delete()
    return redirect('category_detail', category_id=category_id)
    

def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'posts.html', {'all_posts':all_posts})