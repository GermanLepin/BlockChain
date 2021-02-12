from django.shortcuts import render
from .models import Block
from django.views.generic import DetailView

# Create your views here.

def blocks(request):
    new = Block.objects.order_by('-block_time')
    return render(request, 'blocks.html', {'new': new})

class BlockDetailViews(DetailView):
    model = Block
    template_name = 'details_view.html'
    context_object_name = 'blocks'


