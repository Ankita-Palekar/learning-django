from django.http import HttpResponse


def index(request):
    return HttpResponse("List of all blogs here.")
# Create your views here.
