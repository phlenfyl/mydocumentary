from django.shortcuts import get_object_or_404, render
from .models import Documentation

# Create your views here.


def home(request):
    documentations = Documentation.objects.all()
    return render(request, 'maincontent/pagination.html', {'documentations': documentations})



def documentation_detail_view(request, pk):
    documentation = get_object_or_404(Documentation, pk=pk)
    
    # Render the detail template with the documentation context
    return render(request, "maincontent/detail.html", {"documentation": documentation})


from django.http import HttpResponse

def get_ip(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip_address:
        ip_address = ip_address.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')
        
    return HttpResponse(f"Your IP address is {ip_address}")



