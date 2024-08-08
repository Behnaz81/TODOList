from django.forms import ModelForm, Textarea
from .models import Task


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'priority', 'description']
        labels = {
            'title': 'موضوع',
            'description': 'توضیحات',
            'priority': 'اولویت'
        }
        widgets = {
            'description': Textarea(attrs={ 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].label_classes = ('form-label')
        self.fields['priority'].widget.attrs.update({'class': 'form-select'})
        self.fields['priority'].label_classes = ('form-label')
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].label_classes = ('form-label')
