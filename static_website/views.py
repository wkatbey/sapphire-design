from django.shortcuts import render
from django.views.generic import TemplateView, View
from static_website.forms import ContactForm

class Home(View):
    template_name = 'static_website/index.html'

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
        
        form = ContactForm()
        return render(request, self.template_name, {'form': form})