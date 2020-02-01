from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from django.http import *
from django.contrib import auth
# Create your views here.
from .forms import *
from django.contrib.auth.models import User
from myapp.forms import *
from myapp.models import *

def login(request):
    return render(request,'login.html')


def index(request):

    if request.method == 'POST':
        form = Comment_form(request.POST)
        #print (request.POST['text'])
        if form.is_valid():
            print(form.cleaned_data['text'])
            f=form.save(commit=False)
            f.created_by = request.user
            f.save()
            return redirect('login_app:home')
            
    else:
        form = Comment_form()
        data = Comment.objects.all()
        nested_data = Nested_Comment.objects.all()
        
    return render(request,'blog-post.html',{'data':data,
                                            'nested':nested_data})
    
def nested_comment(request):
    form = Nested_Comment_form(request.POST)
    comment_id = request.POST['comment']
    cmt = Comment.objects.get(id=comment_id)
    print (cmt)
    if form.is_valid():
        f=form.save(commit=False)
        f.created_by = request.user
        f.comment = cmt
        f.save()
        return redirect('login_app:home')


def home(request):
    if request.user.is_authenticated():
        return index(request)
    else:
        return login(request)

def auth_view(request):
    #print request.POST,type(request)
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        
        return redirect('login_app:home')
    else:
        return HttpResponseRedirect('/invalid/')
    

def invalid_login(request):
    return render(request,'invalid_login.html')

def logout(request):
    auth.logout(request)
    
    return HttpResponseRedirect('/')

def signup(request):
    if request.method=='POST':
        form=Regforms(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password,
                                     email=email)
            return redirect('login_app:home')
            #user = authenticate(username=username, password=password)
            #login(request, user)
            #return render(request,'login.html')
    else:
        form=Regforms()
    return render(request,'signup.html',{'form':form})




