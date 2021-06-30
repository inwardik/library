from django import forms
from django.forms import ModelForm
from .models import Book
from author.models import Author


class BookForm2(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class MyModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.name} {obj.surname}'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
    name = forms.CharField()
    description = forms.CharField()
    count = forms.IntegerField()
    authors = MyModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

