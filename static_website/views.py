from django.shortcuts import render
from django.views.generic import TemplateView, View
from static_website.forms import ContactForm
<<<<<<< HEAD
from django.core.mail import send_mail

COMPANY_EMAIL = 'katbeywassim@gmail.com'
DEFAULT_SUBJECT = 'Website Inquiry'
=======
>>>>>>> e6a7c0b8cdf8259d3dc106d0df192332b820d37f

class Home(View):
    template_name = 'static_website/index.html'

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
<<<<<<< HEAD
        context = {}
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['inquiry']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['business'] + ' ' + DEFAULT_SUBJECT
            full_name = form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name']

            send_mail(
                subject,
                message,
                from_email,
                [COMPANY_EMAIL],
                fail_silently=True
            )

            print(subject)

            form = ContactForm()

            context['form'] = form
            context['message'] = "We appreciate your inquiry! A member of our team will respond as soon as they can"

            return render(request, self.template_name, context)

=======
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
        
>>>>>>> e6a7c0b8cdf8259d3dc106d0df192332b820d37f
        form = ContactForm()
        return render(request, self.template_name, {'form': form})