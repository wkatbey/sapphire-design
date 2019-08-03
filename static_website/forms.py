from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    business = forms.CharField(label='Company')
    inquiry = forms.CharField(
        label = 'Your Inquiry',
        widget = forms.Textarea(
            attrs = {'rows': 10, 'cols': 50}
        )
    )
