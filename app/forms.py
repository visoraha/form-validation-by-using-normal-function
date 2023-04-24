from django import forms
def check_a(value):
    if value[0]=='a':
        raise forms.ValidationError('cant start with a')
def check_length(value):
    if len(value)<6:
        raise forms.ValidationError('len is low')

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_a,check_length])
    age=forms.IntegerField()
    email=forms.EmailField()