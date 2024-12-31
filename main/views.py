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


