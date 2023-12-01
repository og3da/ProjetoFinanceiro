from django.http import HttpResponse
from django.template import loader


def aprenda_economizar(request):
    template = loader.get_template('plan-eco.html')
    return HttpResponse(template.render())

def negociar_dividas(request):
    template = loader.get_template('plan-div.html')
    return HttpResponse(template.render())
