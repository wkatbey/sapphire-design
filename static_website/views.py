import os
import sendgrid
from sendgrid.helpers.mail import *
from django.shortcuts import render
from django.views.generic import TemplateView, View
from static_website.forms import ContactForm
from django.core.mail import send_mail

COMPANY_EMAIL = 'katbeywassim@gmail.com'
DEFAULT_SUBJECT = 'Website Inquiry'

class Home(View):
    template_name = 'static_website/index.html'

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        context = {}
        form = ContactForm(request.POST)
        if form.is_valid():
            # sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
            message = form.cleaned_data['inquiry']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['business'] + ' ' + DEFAULT_SUBJECT
            full_name = form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name']

            content = "text/plain", "Hello, Email!"

            send_mail(subject, message, from_email, [COMPANY_EMAIL], fail_silently=False)
     
            form = ContactForm()

            context['form'] = form
            context['message'] = "We appreciate your inquiry! A member of our team will respond as soon as they can"

            return render(request, self.template_name, context)

        form = ContactForm()
        return render(request, self.template_name, {'form': form})