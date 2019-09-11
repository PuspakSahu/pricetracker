from django import forms

class new_entry(forms.Form):
	url=forms.CharField(max_length=1000,widget=forms.TextInput(attrs={'class':'form-control','size':40}))
	email=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
	price=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))