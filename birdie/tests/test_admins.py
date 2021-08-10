import pytest 
from django.test  import LiveServerTestCase ,TestCase

from mixer.backend.django import mixer

from  .. import admin

from .. import models
pytestmark = pytest.mark.django_db

from django.contrib.admin.sites import AdminSite


class TestPostAmdin:

    def test_except(self):
        obj = mixer.blend('birdie.Post')
        site =AdminSite() #helps us to test our own custom ModelAdmin custom ListVIew
        post_admin=admin.PostAdmin(models.Post, site)


        obj = mixer.blend('birdie.Post',body='Hello World')
        result = post_admin.excerpt(obj)
        assert result =='Hello','Should return first few characters'