from django.http import HttpResponse
from django.template import loader

# Create your views here.
def calc_sal_liq(request):
    template = loader.get_template('calc-sal-liquido.html')
    return HttpResponse(template.render())