import pytest 
from django.test  import LiveServerTestCase ,TestCase

from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db
#it protects from writing to the database,
#always go the previous project ,and copy and paste


class TestPost(LiveServerTestCase):

    def test_model(self):
        obj=mixer.blend('birdie.Post')
        assert obj.pk == 2,'Should create a Post instance'

    def test_get_excerpt(self):
        obj = mixer.blend('birdie.Post',body='Hello World!')
        result =obj.get_excerpt(5) 

        assert result == 'Hello','Should return first few characters'
        # return None ,This is like a debug documentation of messages,what the tests should do


#def test_init(self):
# obj = mixer.blend('birdie.post',message='Hello')
#assert obj.pk == 1,'Shoud save an instance'
#body fixture from results 
# post =  Post()
#this method of testing our models is very tedious ,so using mixer is goood

# post.message = "Hello"
# post.save()
# mixer.blend('birdie.post',message=notifcation saying saying for failure or success')
