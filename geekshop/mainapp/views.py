from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'mainapp/index.html')

def products(request):
    return render(request, 'mainapp/products.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')

def iphoneX(request):
    return render(request, 'mainapp/iphoneX.html')

def iphone8(request):
    return render(request, 'mainapp/iphone8.html')