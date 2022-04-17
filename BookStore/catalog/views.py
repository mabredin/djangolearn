from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.views import generic
from .models import Book, BookInstance, Genre, Admission


class HomePageView(generic.ListView):
    template_name = 'catalog/index.html'
    context_object_name = 'latest_books_list'

    def get_queryset(self):
        return Book.objects.order_by('-id')[:5]


class CatalogView(generic.ListView):
    model = Genre
    template_name = 'catalog/catalog.html'
    context_object_name = 'list_genres'

    def get_queryset(self):
        return Genre.objects.all()


class GenreView(generic.DetailView):
    model = Genre
    template_name = 'catalog/genre.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        context['genre_list'] = Genre.objects.all()
        return context

#     def get_queryset(self):
#         return Genre.objects.filter(id=self.kwargs['pk'])


class DetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        context['genre_list'] = Genre.objects.all()
        return context


def about(request):
    return render(request, 'not_ready.html')


def recommendations(request):
    return render(request, 'not_ready.html')