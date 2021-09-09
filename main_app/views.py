from django.shortcuts import render, redirect
from .models import Shoe
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create the view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def shoes_index(request):
    shoes = Shoe.objects.filter(user=request.user)
    return render(request, 'shoes/index.html', {'shoes': shoes})

@login_required
def shoes_detail(request, shoe_id):
    shoe = Shoe.objects.get(id = shoe_id)
    return render(request, 'shoes/detail.html', { 'shoe': shoe })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('shoes_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class ShoeCreate(LoginRequiredMixin,CreateView):
    model = Shoe
    fields = '__all__'
    success_url='/shoes/'

@LoginRequiredMixin
class ShoeUpdate(UpdateView):
    model = Shoe
    fields ='__all__'

    def form_valid(self, form):
        return super().form_valid(form)

@LoginRequiredMixin
class ShoeDelete(DeleteView):
    model = Shoe
    success_url = '/shoes/'