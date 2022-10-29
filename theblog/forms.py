from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            'title': form.TextInput(attrs={'class': 'form-control'}),
            'title_tag': form.TextInput(attrs={'class': 'form-control'}),
            'author': form.Select(attrs={'class': 'form-control'}),
            'body': form.Textarea(attrs={'class': 'form-control'}),
        }
        