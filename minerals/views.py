from django.shortcuts import get_object_or_404, render
from django.db.models import Q


from . import models


# Create your views here.
def index(request):
    minerals = models.Mineral.objects.all()
    return render(request, 'index.html', {'minerals': minerals})


def detail(request, pk):
    mineral = get_object_or_404(models.Mineral, pk=pk)
    return render(request, 'detail.html', {'mineral': mineral})


def search(request):
    """Searches database by mineral name for entered free text term"""
    term = request.GET.get('q')
    minerals = models.Mineral.objects.filter(name__icontains=term)
    return render(request, 'index.html', {'minerals': minerals})


def group(request, group):
    """filters database and returns all minerals by mineral category"""
    minerals = models.Mineral.objects.filter(group=group)
    return render(request, 'index.html', {'minerals': minerals})


def letter(request, letter):
    """filters database and returns all minerals starting with the first letter"""
    minerals = models.Mineral.objects.filter(name__startswith=letter)
    return render(request, 'index.html', {'minerals': minerals})
