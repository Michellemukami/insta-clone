

from django import forms
from .models import Article

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['editor']
        widgets = {
            'vote': forms.CheckboxSelectMultiple(),
        }
class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
class CommentForm(forms.Form):
    Comment = forms.CharField(label='comment',max_length=100)

