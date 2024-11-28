from .models import Article
from .forms import SearchForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import WebsiteForm

def home(request):
    form = SearchForm()
    results = []
    article_quantity = 0 

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Article.objects.filter(title__icontains=query) | Article.objects.filter(url__icontains=query)
            article_quantity = results.count()

    return render(request, 'search_engine/index.html', {
        'form': form,
        'results': results,
        'article_quantity': article_quantity,
    })

def dashboard(request):
    websites = Article.objects.all()
    return render(request, 'search_engine/dashboard.html', {'websites': websites})

def add_website(request):
    if request.method == "POST":
        form = WebsiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = WebsiteForm()
    return render(request, 'search_engine/add_website.html', {'form': form})

def delete_website(request, pk):
    website = get_object_or_404(Article, pk=pk)
    website.delete()
    return redirect('dashboard')
