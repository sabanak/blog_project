from django import forms
from . models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','author','desc')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
            # 'post_date':forms.Select(attrs={'class':'form-control'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','desc')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }