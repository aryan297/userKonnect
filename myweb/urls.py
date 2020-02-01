
from django.conf.urls import url,include
from django.contrib import admin
from myapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index),
    
    url(r'^blog_login/',include('newapp.urls',namespace='login_app'))
]
