from django.http import HttpResponse
from django.template import loader

# Create your views here.
def tesouro_direto(request):
    template = loader.get_template('tesouro-direto.html')
    return HttpResponse(template.render())

def inv_longo_prazo(request):
    template = loader.get_template('inv-longo.html')
    return HttpResponse(template.render())

def inv_curto_prazo(request):
    template = loader.get_template('inv-curto.html')
    return HttpResponse(template.render())