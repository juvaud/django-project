from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ContactForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            context['text'] = form.cleaned_data
            print(form.cleaned_data)
            pass
            #print('YYAS')
    else:
        form = ContactForm()
        context = {'form': form}
    return render(request, 'index.html', context=context)


class AboutPageView(TemplateView):
    template_name = 'about.html'


