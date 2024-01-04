from django.http import HttpResponse
#from pyats.topology import Testbed, Device


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the newapp index.")