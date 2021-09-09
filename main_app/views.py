from django.shortcuts import render, redirect
from .models import Shoe , Photo
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'shoe-collector'

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


def add_photo(request, shoe_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
		# uuid.uuid4().hex generates a random hexadecimal Universally Unique Identifier
    # Add on the file extension using photo_file.name[photo_file.name.rfind('.'):]
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to cat_id or cat (if you have a cat object)
      photo = Photo(url=url, shoe_id=shoe_id)
      # Remove old photo if it exists
      shoe_photo = Photo.objects.filter(shoe_id=shoe_id)
      if shoe_photo.first():
        shoe_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('shoes_detail', shoe_id=shoe_id)

class ShoeCreate(LoginRequiredMixin,CreateView):
    model = Shoe
    fields = ['name', 'brand', 'colorway', 'size']
    success_url='/shoes/'


class ShoeUpdate(LoginRequiredMixin, UpdateView):
    model = Shoe
    fields = ['name', 'brand', 'colorway', 'size']

    def form_valid(self, form):
        return super().form_valid(form)


class ShoeDelete(LoginRequiredMixin,DeleteView):
    model = Shoe
    success_url = '/shoes/'