from django.shortcuts import render, redirect
from BookApp.models import Book

# Create your views here.

def homePage(request):
    #fetching the data
    data = Book.objects.all()
    context = {}
    context['books'] = data
    return render(request,'home.html',context)

def addBook(request):
    if request.method == "GET" :
        return render(request,'addbook.html')
    else:
        #fetch data
        t = request.POST['title']
        a = request.POST['author']
        p = request.POST['price']
        # insert the row in database
        b = Book.objects.create(title = t, author = a, price=p)
        b.save()
        # return render(request, 'home.html') # empty , no data 
        # #fetching the data
        # data = Book.objects.all()
        # context = {}
        # context['books'] = data
        # return render(request,'home.html',context)
        # we need to execute --> homePage(), but we cant call it here
        # so, we need to redirect
        return redirect('/home')
    
def deleteBook(request,bookid):
    # print('delete book id:',bookid)
    b = Book.objects.filter(id = bookid)
    b.delete()
    # return render(request,'home.html')
    return redirect('/home')
       
def updateBook(request,bookid):
    if request.method == "GET":
        print('update book id:',bookid)
        b = Book.objects.filter(id = bookid)
        '''
        b is a QuerySet, and it can have
        all book objects returned by database, based on condition.
        we are filtering book data based on PK 'id', so there will be only 1 book object.
        that book object is present at index 0, so we need to send b[0] to template
        '''
        # print(b[0].title)
        context = {}
        context['book'] = b[0]
        return render(request,'updatebook.html',context)
    else:
        #fetch the data
        t = request.POST['title']
        a = request.POST['author']
        p = request.POST['price']
        b = Book.objects.filter(id = bookid) # fetch the book object based on id
        b.update(title = t, author = a,price = p) # update will update all the books in b with new t,a,p
        return redirect('/home')