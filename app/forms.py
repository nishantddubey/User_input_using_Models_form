from django import forms
from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
        

class WebpageForm(forms.ModelForm):
    class Meta:
        model = Webpage
        fields = '__all__'
        # labels = {'topic_name':'TN'}
        # widgets = {'url':forms.PasswordInput()} 
        
        
class AccessrecordForm(forms.ModelForm):
    class Meta:
        model = Accessrecord
        fields = '__all__'