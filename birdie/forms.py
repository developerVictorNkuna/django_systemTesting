from django import forms 
from . import models 
class PostForm(forms.ModelForm): 
    class Meta: 
        model =models.Post 
        fields = ('body',)






    def clean_body(self): 
        """clean body,for every field of my model, there is a field clean method write clean field namec
        clean_field_name"""
        
        data =self.cleaned_data.get('body')
        if len(data) <=5: 
            raise forms.ValidationError('Message too short')
        return data 
        