from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Destination

# Create your views here.


def index(request):

    # dest1 = Destination()
    # dest1.name = 'Dhaka'

    # dest1.desc = 'The city of horror'

    # dest1.price = 1200

    # dest1.img = 'destination_1.jpg'

    # dest1.offer = True

    # dest2 = Destination()
    # dest2.name = 'Chittagong'

    # dest2.desc = 'The city of beaches'

    # dest2.price = 1500

    # dest2.img = 'destination_2.jpg'

    # dest2.offer = False

    # dest3 = Destination()
    # dest3.name = 'Bogura'

    # dest3.desc = 'Another planet of Bangladesh'

    # dest3.price = 2000

    # dest3.img = 'destination_3.jpg'

    # dest3.offer = False

    # dests = [dest1, dest2, dest3]

    # return render(request, 'index.html', {'dest1': dest1, 'dest2': dest2, 'dest3': dest3}) my method, it works also
    # context must be a dictionary, whwre as we are passing or creating a dictionary with key 'dests' which value is a list of objects dests, simple :)

    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests': dests})


def about(request):

    return render(request, 'about.html', {})
