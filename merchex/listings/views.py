from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

# Create your views here.
def hello(request):
    bands=Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})
    

def about(request):
    return HttpResponse('<h1>About us</h1> <p>We love merch!</p>')

def listings(request):
    listings=Listing.objects.all()
    return HttpResponse(f"""
    <h2> List of the concerts :</h2>
    <p>Coming soon...</p>
    <ul>
    <li>{listings[0].title}</li>
    <li>{listings[1].title}</li>
    <li>{listings[2].title}</li>
    </ul>
    """)

def contactus(request):
    return HttpResponse('<p>Contactez nous ici</p>')