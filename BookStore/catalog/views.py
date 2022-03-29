from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from .models import Book, BookInstance


class IndexView(generic.ListView):
    template_name = 'catalog/index.html'
    context_object_name = 'list_books'
    paginate_by = 5

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Book.objects.all()

    # def get(self, request, *args, **kwargs):
    #     new_books = Book.objects.filter(genre=1)
    #     # popular_books = BookInstance.check__set.filter()
    #     context = self.get_context_data()
    #     return self.render_to_response(context)