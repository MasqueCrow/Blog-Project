from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        # To get custom styling to forms, adding widget attribute
        # classnames refers to the external css library used
        # 'textinputclass' and 'postcontent are custom classes
        widgets = {

            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={ 'class':'editable medium-editor-textarea postcontent'})
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        # Similer kind of widgets as PostForm, no 'postcontent' custom class
        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={ 'class':'editable medium-editor-textarea'})
        }
