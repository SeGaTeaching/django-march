from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app(request):
    """
    Eine einfache View-Funktion, die 'Hello, World!' zurückgibt.
    """
    
    html_content = f"""<h1>Hello World</h1>
                    <p>Das ist HTML aus der Django myapp App Views Datei</p>
                    <p>Methode: {request.method}
                    """
    
    #return HttpResponse(html_content)
    
    return render(request, "myapp/index.html", {})

def marion(request):
    return HttpResponse("<h1>Hallo Marion</h1>")

def john(request):
    return HttpResponse("<h1>Hallo John</h1>")

def user(request, name):
    return HttpResponse(f"Hallo, {name}")

def product_details(request, product_id):
    return HttpResponse(f"you requested the Product with ID: {product_id}")
