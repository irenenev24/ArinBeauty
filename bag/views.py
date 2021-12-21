from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """A view to return the shoppng bag contents page"""

    return render(request, 'home/index.html')
