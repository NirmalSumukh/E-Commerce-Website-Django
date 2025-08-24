from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column, Submit
# from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ["title", "category", "excerpt", "content",
                  "featured", "status", "tags"]
        # widgets = {"content": CKEditorUploadingWidget(config_name="blog")}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                "Post details",
                Row(Column("title", css_class="col-md-8"),
                    Column("status", css_class="col-md-4")),
                "category",
                "excerpt",
                "content",
                "featured",
                "tags",
            ),
            Submit("submit", "Save", css_class="btn btn-primary")

        )
