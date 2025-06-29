from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .models import Movie, Comment, CustomUser
from .forms import CustomRegisterForm, MovieForm, CommentForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('movie_list')
    else:
        form = CustomRegisterForm()
    return render(request, 'movie_register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('movie_list')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

@login_required
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'movie_form.html', {'form': form})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    comments = movie.comments.all()
    average = movie.average_rating()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.author = request.user
            comment.save()
            return redirect('movie_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'movie_detail.html', {'movie': movie, 'comments': comments, 'form': form, 'average': average})

@login_required
def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', pk=pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie_form.html', {'form': form})

@login_required
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('movie_list')

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})