from django.shortcuts import render
from django.http import HttpResponse

# Create the view
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def shoes_index(request):
    # sneakers = Sneaker.objects.all()
    return render(request, 'shoe/index.html', {'shoes': shoes})