from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
<<<<<<< HEAD
    email = forms.CharField(label='Email')
=======
>>>>>>> e6a7c0b8cdf8259d3dc106d0df192332b820d37f
    business = forms.CharField(label='Company')
    inquiry = forms.CharField(
        label = 'Your Inquiry',
        widget = forms.Textarea(
            attrs = {'rows': 10, 'cols': 50}
        )
    )
