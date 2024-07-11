from django import forms
from django_editorjs_fields import EditorJsWidget
from articles.models import Article

class ArticleCreationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title' , 'img' , 'description' , 'status' , 'body' , 'tags']
        labels = {
            'tags' : "برچسب ها"
        }
        widgets = {
            'title' : forms.TextInput(attrs={"placeholder" : "عنوان ..."}),
            'description' : forms.Textarea(attrs={"placeholder" : "توضیحات..."}),
            'tags' : forms.TextInput(attrs={"placeholder" : "برچسب ها"}),
            'img' : forms.FileInput(attrs={'class' : "custom-file-upload"}),
            'status' : forms.Select(attrs={"title" : "وضعیت"})
        }
        help_texts = {
            "tags" : "با ( ، ) میتوانید تا ۵ برچسب وارد کنید"
        }
        exclude = []


    def set_author(self , user):
        Article.author = user
