from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Neighbourhood
from .forms import UserRegisterForm, PostPictureForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    posts = Neighbourhood.objects.all()
    return render(request, 'index.html', { 'posts': posts })



def image_form(request):
    if request.method == 'POST': 
        form = PostPictureForm(request.POST, request.FILES) 
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = request.user.profile
            form.save()
            return redirect('home') 
    else: 
        form = PostPictureForm() 
    return render(request, 'image_form.html', {'form' : form}) 
