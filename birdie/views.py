from django.shortcuts import render ,redirect
from django.views import generic
from django.views.generic import TemplateView  ,UpdateView
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator 
from  . models import*
from . forms import*
from django.http import Http404
# Create your views here.
from django.core.mail import send_mail
import stripe
class HomeView(TemplateView): 
    template_name  ="birdie/home.html"


class AdminView(TemplateView): 
    template_name  ="birdie/admin.html"

    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs): 
        #BREAKPOINT,to invoke the debugger ,ensure that the user has to be login
        # import pdb; pdb.set_trace() 
        #how to protect CBV overides url dispatch,return supper call
        #
        """this fucntion overrides the class based view to protect ,
        a view from certian users essentially testing  authentication""" 
        return super(AdminView,self).dispatch(request,*args,**kwargs)

class PostUpdateView(UpdateView): 
    """this view edits existing post,
    anyone can post a view no need to log in"""

    model =Post
    form_class =PostForm 
    template_name ='birdie/update.html'
    success_url ='/'

    def post(self,request,*args,**kwargs): 
        if getattr(request.user,'first_name',None) =='VictorNkuna':
            raise(Http404)
        return super(PostUpdateView,self).post(request,*args,**kwargs)

class PayementView(generic.View): 
    def post(self,request,*args,**kwargs): 
        charge = stripe.Charge.create(
                amoount=100,
            currency='zar',
            description ='',
            token =request.POST.get('token')
        )
        send_mail(
                'Payment received',
                'Charge {} succeded!'.format(charge['id']),
                'server@example.com',
                ['admin@example.com',],
                )
        
        return redirect('/')

        #patch mock,returned function,and come wwith returned values
