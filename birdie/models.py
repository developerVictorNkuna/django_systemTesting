from __future__ import unicode_literals

from django.db import models
# from django.db import models

# Create your models here.


class Post(models.Model):
    body= models.TextField(max_length=200,default='')

    def get_excerpt(self,char):
        return self.body[:char]

    # def get_absolute_url(self): 
    #     return f'{self.id}'
    