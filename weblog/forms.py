from django import forms

from weblog.models import WeBlog


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class WeBlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = WeBlog
        exclude = ('slug', 'count_of_views', 'is_published')
