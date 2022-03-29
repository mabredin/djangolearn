from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.views import generic
from .models import Book, BookInstance, Genre


class HomePageView(generic.ListView):
    template_name = 'catalog/index.html'
    context_object_name = 'list_books'
    paginate_by = 5

    def get_queryset(self):
        return Book.objects.all()

    # def get(self, request, *args, **kwargs):
    #     new_books = Book.objects.filter(genre=1)
    #     # popular_books = BookInstance.check__set.filter()
    #     context = self.get_context_data()
    #     return self.render_to_response(context)


class GenresView(generic.ListView):
    template_name = 'catalog/genres.html'
    context_object_name = 'list_genres'

    def get_queryset(self):
        return Genre.objects.all()


def about(request):
    return render(request, 'not_ready.html')


def recommendations(request):
    return render(request, 'not_ready.html')