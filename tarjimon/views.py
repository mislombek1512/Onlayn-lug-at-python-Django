from django.shortcuts import render
from django.http import HttpResponse
from deep_translator import GoogleTranslator



def index(request):
    text = request.GET.get('translate', '')
    if text and text != '':
        res = GoogleTranslator(source='auto', target='uz').translate(text)
    else:
        res = None
    return  render(request, 'index.html', {'translate':text, 'res':res})

def hello(request):
    return  HttpResponse('Mustafo')