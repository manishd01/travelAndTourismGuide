from django import forms

class sign_up_add_form(forms.Form):
    first_name= forms.CharField(null=false, max_length=250, required=True)