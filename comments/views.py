from django.shortcuts import render
from django.http import HttpResponse
from .models import Comments
from .models import Product


def index(request):
    product = Product.objects.all()

    return render(request, 'comments/index.html', {'product': product})


def test(request):
    comments = Comments.objects.order_by('-created_add')

    return render(request, 'comments/comments.html', {'comments': comments})
