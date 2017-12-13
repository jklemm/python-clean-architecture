from django import forms


class AddStudentForm(forms.Form):
    name = forms.CharField(required=True, label='Name', widget=forms.TextInput())
    age = forms.IntegerField(required=True, label='Age')
