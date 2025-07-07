from django.shortcuts import render
from django.http import HttpResponse
from .models import InternshipOffers

# Create your views here.
def main(request):
    # Fetch all internship offers
    internships = InternshipOffers.objects.all().order_by('-created_at')
    
    context = {
        'internships': internships,
    }
    
    return render(request, 'internships/dashboard.html', context)
