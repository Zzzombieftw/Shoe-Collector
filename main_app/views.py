from django.shortcuts import render
from .models import Shoe
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create the view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def shoes_index(request):
    shoes = Shoe.objects.all()
    return render(request, 'shoes/index.html', {'shoes': shoes})

def shoes_detail(request, shoe_id):
    shoe = Shoe.objects.get(id = shoe_id)
    return render(request, 'shoes/detail.html', { 'shoe': shoe })

class ShoeCreate(CreateView):
    model = Shoe
    fields = '__all__'
    success_url='/shoes/'

class ShoeUpdate(UpdateView):
    model = Shoe
    fields ='__all__'

    def form_valid(self, form):
        return super().form_valid(form)

class ShoeDelete(DeleteView):
    model = Shoe
    success_url = '/shoes/'