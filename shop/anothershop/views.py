from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

products = [
    {'id':1, 'title': 'Skirt', 'size': 'L', 'price': 2000},
    {'id':1, 'title': 'Skirt', 'size': 'L', 'price': 2000},
    {'id':1, 'title': 'Skirt', 'size': 'L', 'price': 2000},
    {'id':1, 'title': 'Skirt', 'size': 'L', 'price': 2000},
    {'id':1, 'title': 'Skirt', 'size': 'L', 'price': 2000},
]

def productsView(request):
    return render(request, 'shop/products.html', context={'products': products})

def product(request):
    return render(request, 'shop/product.html', id='id')

def index(request):
    header = "Данные пользователя"
    langs = ['C', 'C++', "Python", 'Java', 'Javascript']
    user = {'name': 'Vasilii', 'subname': 'Pupkin'}
    address = ("Mira", 12, 147)

    data = {'header': header, "langs": langs, 'user': user, 'address':address}
    return render(request, 'shop/index.html', context=data)
def about(request):
    data = {'name': 'Grisha', "interests": 'Videogames'}
    return render(request, 'shop/about.html')
def contacts(request):
    return render(request, 'shop/contacts.html')

