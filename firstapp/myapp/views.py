from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


def index(req):
    dict = [
        {'name': 'ghozt'},
        {'name': 'react'}
    ]
    showLaguage = False
    menu = [
        {
            'name' : '🍕' ,
            'price' : 1.89 ,
            'quantity' : 10
        } ,
        {
            'name' : '🧀' ,
            'price' : 2.00 ,
            'quantity' : 12
        } ,
        {
            'name' : '🍔' ,
            'price' : 3.99 ,
            'quantity' : 5
        } ,
        {
            'name' : '🥨' ,
            'price' : 0.99 ,
            'quantity' : 20
        } ,
    ]
    print(req)
    return render(req, 'myapp/index.html', {
        'useDict': dict,
        'showLanguage': showLaguage ,
        'menu' : menu
    })
