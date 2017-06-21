from django import forms

class UserForm(forms.Form):

    title = forms.CharField(label='title', max_length=256, widget = forms.TextInput(attrs={'class':'form-control'}))
    
    language = forms.CharField(label='language', max_length=256, widget = forms.TextInput(attrs={'class':'form-control'}))

    snippet = forms.CharField(label='snippet', max_length=10000, widget = forms.Textarea(attrs={'class':'form-control'}))

    description = forms.CharField(label='description', max_length=256, widget = forms.TextInput(attrs={'class':'form-control'}))
