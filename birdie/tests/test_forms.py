import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser 
from .. import views 
from mixer.backend.django import mixer
from .. import  forms 
pytestmark = pytest.mark.django_db #this tells pytest that we can do db access


class TestPostForm: 
    def test_form(self): 
        form =forms.PostForm(data={"body":''})
        assert form.is_valid() == False ,"Should be invalid if no data is given"

        form = forms.PostForm(data ={'body':'Hello'})
        assert form.is_valid() is False ,'Should be invlaid if too short'

        assert 'body' in form.errors,'Should have body field error'
        
        form  = forms.PostForm(data={'body':'Hello World !!!!!!!'})
        assert form.is_valid() is True ,'Should be valid if long enough'
