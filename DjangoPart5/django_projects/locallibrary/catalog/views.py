from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

# Create your views here.
from django.http import HttpResponse


def index(request):
    """View function for home page of site."""
    
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_availlable = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    
    
    num_genres = Genre.objects.filter(name__icontains='f').count()
    
    num_word_specific_books = Book.objects.filter(title__icontains='animal').count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_word_specific_books': num_word_specific_books,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
