from django.shortcuts import *
from .forms import *
from .models import *
from django.http import *
# Create your views here.

def index(request):
    return render(request,'index.html')

def blog(request):
    if request.method == 'POST':
        form = Comment_form(request.POST)
        print (request.POST['text'])
        if form.is_valid():
            print(forms.cleaned_data['text'])
            f=form.save(commit=False)
            f.created_by = request.user
            f.save()
            return redirect('blog')
            
    else:
        form = Comment_form()
    return render(request,'blog-post.html',{'form':form})



