from django import forms

from registration.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)
