from django import forms
from .models import post
class create_post_form(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter title...................'}))
    content=forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    content=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter content .............'}))
    class Meta:
        model=post
        fields=['title','content']