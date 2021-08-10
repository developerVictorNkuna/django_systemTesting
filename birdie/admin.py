from django.contrib import admin
from  . models import *
# from django.contrib.auth import Postf
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    model =Post(body="Ke na nna kgosi , ya tshelete ,hosi Matompo of the Zobo ra ingwe Mapangwube")
    list_display=('excerpt',)

    def excerpt(self, obj):

        return obj.get_excerpt(5)
admin.site.register(Post,PostAdmin)
    #filer admin panel based on these
