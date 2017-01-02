from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class home(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Add this view
class about(TemplateView):
    template_name = "about.html"

class contact(TemplateView):
    template_name = "contact.html"

class blog(TemplateView):
    template_name = "post_list.html"