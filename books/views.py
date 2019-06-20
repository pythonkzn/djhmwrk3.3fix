import datetime
from django.shortcuts import render
from .models import Book


def books_view(request, year=None, month=None, day=None, book_name=None):
    books = Book.objects.all()
    prev_date = '-'
    next_date = '-'
    book_list = []

    template = 'books/books_list.html'

    if year:
        url_date = datetime.date(year, month, day)
    else:
        url_date = None

    for book in books:
        book.str_date = str(book.pub_date)
        book_list.append(book)
    book_list = sorted(book_list, key=lambda k: k.pub_date)
    i = 0

    if url_date is not None:
        for book in book_list:
            if book.pub_date == url_date:
                if (i >= 1) and (i < (len(book_list)-1)):
                    prev_date = str(book_list[i-1].pub_date)
                    next_date = str(book_list[i+1].pub_date)
                elif (i < 1) and (i < (len(book_list)-1)):
                    prev_date = '-'
                    next_date = str(book_list[i + 1].pub_date)
                elif (i >= 1) and (i >= (len(book_list)-1)):
                    prev_date = str(book_list[i-1].pub_date)
                    next_date = '-'
                book_list = [book]
            i += 1
    else:
        book_list = books


    context = {'books': book_list, 'prev_date': prev_date, 'next_date': next_date}

    return render(request, template, context)
