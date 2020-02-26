from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile,Neighbourhood
# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    posts = Neighbourhood.objects.all()
    return render(request, 'index.html', { 'posts': posts })