from django.shortcuts import render,redirect,reverse
from django.shortcuts import HttpResponse
from django.db import connection

def get_corsor():
    return connection.cursor()

def index(request):
    cursor = get_corsor()
    cursor.execute("select id,name,author from book")
    books = cursor.fetchall()
    return render(request,'index.html',context={"books":books})

def add_book(request):
    if request.method == 'GET':
        return render(request,'add_book.html')
    else:
        name = request.POST.get("name")
        author = request.POST.get("author")
        cursor = get_corsor()
        cursor.execute("insert into book(id,name,author) values('%s','%s','%s')" % (1,name, author))
        return redirect(reverse('index'))

def book_detail(request,book_id):
    cursor = get_corsor()
    cursor.execute("select id,name,author from book where id=%s") % book_id
    book = cursor.fetchone
    return render(request,'book_detail.html',context={"book":book})
