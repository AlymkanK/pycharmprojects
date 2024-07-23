from django import forms
from django.forms import widgets


class TaskForm(forms.Form):
    description = forms.CharField(
        max_length=50,
        required=True,
        label = 'Название',
        widget = widgets.Input(attrs={'placeholder': 'Задача'}),
    )
    status = forms.CharField(
        max_length=50,
        required=False,
        label='Статус',
        widget = widgets.Textarea(attrs={'cols': 20, 'rows': 5, 'placeholder': 'Статус'}))
    date = forms.DateField(required=True, label='Срок выполнения')