from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView, CreateView
from django.views.decorators.http import require_http_methods
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from .models import Category, Book
from .form import createCategoryForm, createBookForm


class Createcategory(CreateView):
    model = Category
    fields = ['name']
    template_name = 'book/category_create.html'
    success_url = reverse_lazy('book:view_category')


@require_http_methods(['GET', 'POST'])
def add_book(request):
    """ View to render form page"""
    content = {'title': 'Home'}
    form = createBookForm()
    if request.method == 'POST':
        form = createBookForm(request.POST)
        if form.is_valid():
            new_book = form.save()
            return redirect('book:view_book')
    content['category_form'] = form
    return render(request, 'book/create_book.html', content)


class ListCategory(ListView):
    model = Category
    template_name = 'book/view_category.html'

    # def get_context_data(self):
    #     pass

    def get_queryset(self):
        queryset = super(ListCategory, self).get_queryset()
        query_string = self.request.GET.get('q', '')
        queryset = queryset.filter(Q(name__icontains=query_string))
        return queryset


class ListBook(ListView):
    """docstring for ClassName"""

    model = Book
    template_name = 'book/view_book.html'

    def get_queryset(self):
        queryset = super(ListBook, self).get_queryset()
        query_string = self.request.GET.get('q', '')
        queryset = queryset.filter(Q(name__icontains=query_string))
        return queryset
