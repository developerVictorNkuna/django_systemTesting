import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser 
from django.http import  Http404
pytestmark = pytest.mark.django_db #this tells pytest that we can do db access
from mock import*
from django.core import mail
import stripe
from mixer.backend.django import mixer
from .. import views
pytestmark = pytest.mark.django_db
class TestHomeView: 
    def test_annonymous(self): 
        req = RequestFactory().get('/')
        resp = views.HomeView.as_view()(req) 
        assert resp.status_code == 200,"Should be callable by anyone" 


class TestAdminView: 
    def test_annonymous(self): 
        req = RequestFactory().get('/')
        req.user = AnonymousUser()  
        resp = views.AdminView.as_view()(req) 
        assert 'login' in resp.url  

    def test_superuser(self): 
        user = mixer.blend('auth.user',is_superuser=True) 
        #baked up model,lives in auth,we can create objects
        #
        req = RequestFactory().get('/') 
        req.user = user 
        resp = views.AdminView.as_view()(req) 
        assert resp.status_code == 200 ,'Authenticated user can access '

    
class TestPostUpdateView:
    def test_get(self):
        req = RequestFactory().get('/')
        obj =mixer.blend('birdie.Post')
        req.user = AnonymousUser()  
        resp =views.PostUpdateView.as_view()(req,pk=obj.pk)
        assert resp.status_code  == 200,'Should be callable by anyone'







    def test_post(self):
        post=mixer.blend('birdie.Post')
        data = {'body':'New Body Text!'}
        req = RequestFactory().post('/',data=data)
        #data passed to request_post of the Django
        req.user = AnonymousUser()  

        resp =views.PostUpdateView.as_view()(req,pk=post.pk)
        assert resp.status_code  == 302,'Should redirect to success view'
        post.refresh_from_db() #use mixer,mixer will fill some random text,post data some text we know,our db must refreshed,compare body with text we expect
        assert post.body =='New Body Text!','Should update the post'








def test_security(self): 
    """functionality of our,
    mixer can create user,attach user object to the request object,
    pytest.raises"""
    user =mixer.blend('auth.User',first_name='VictorNkuna')
    post =mixer.blend('bridie.Post')
    req = RequestFactory().post('/',data={}) #why empty?
    req.user =user 
    with pytest.raises(Http404):#put Http404 excerption class part of django
        views.PostUpdataeView.as_view()(req,pk=post.pk)



class TestPaymentView: 
    @patch('birdie.views.stripe')
    def test_payment(self,mock_stripe): 
        mock_stripe.Charge.return_value ={'id':234}
        req = RequestFactory().post('/',data={'token':123})
        resp = views.PayementView.as_view()(req)
        assert resp.status_code ==302 ,'should redirect to success_url'
        assert len(mail.outbox) ==1,'Should send an email'
