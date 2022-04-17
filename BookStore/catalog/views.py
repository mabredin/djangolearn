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
        return Book.objects.order_by('-id')[:6]


class CatalogView(generic.ListView):
    model = Genre
    template_name = 'catalog/catalog.html'
    context_object_name = 'list_genres'

    # def get_context_data(self, *args, **kwargs):
    #     self.object_list = super().get_queryset()
    #     context = super(GenresView, self).get_context_data(*args, **kwargs)

    def get_queryset(self):
        return Genre.objects.all()

    # def get(self, request, *args, **kwargs):
    #     books = Book.objects.all()
    #     genres = Genre.objects.all()
    #     context = {}
    #     context.update(books=books, genres=genres)
    #     return self.render_to_response(context)


class GenreView(generic.ListView):
    model = Genre
    template_name = 'catalog/genre.html'
    context_object_name = 'genre'

    def get_queryset(self):
        return Genre.objects.filter(id=self.kwargs['pk'])


class DetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/detail.html'

    def get_queryset(self):
        return Book.objects.all()


def about(request):
    return render(request, 'not_ready.html')


def recommendations(request):
    return render(request, 'not_ready.html')