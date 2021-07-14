from django.shortcuts import render
from django.http import HttpResponse
from .models import Comments
from .models import Product
import json
from django.http import HttpResponse
from urllib.parse import unquote as decode_url
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage


# from db_from_vue.models import db_fro_vue, User


def index(request):
    product = Product.objects.all()
    comments = Comments.objects.order_by('-created_add')
    return render(request, 'comments/index.html', {'product': product, 'comments': comments})


def test(request):
    comments = Comments.objects.order_by('-created_add')
    return render(request, 'comments/comments.html', {'comments': comments})


def get_request(request):
    dict_list = {}
    for key, value in request.POST.items():
        dict_list.update({key: value})
    for key, value in request.FILES.items():
        dict_list.update({key: value})
    for key, value in request.GET.items():
        dict_list.update({decode_url(key): decode_url(value)})
    try:
        for key, value in json.loads(request.body).items():
            dict_list.update({key: value})
    except:
        pass
    return dict_list


@csrf_exempt
def get_comments(request):
    myfile = request.FILES['image']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    print('СМОТРИ НИЖЕ')
    print(myfile)
    print(fs)
    print(filename)
    print(uploaded_file_url)
    data = get_request(request)
    print(f'{data = }')
    comments = Comments.objects.create(full_name=data['full_name'],
                                       comment=data['comment'],
                                       email=data['email'],
                                       rating=data['rating'],
                                       photo_comments=request.FILES['image'])
    return HttpResponse(status=200)


@csrf_exempt
def post_comments(response):
    dict_list_comments = []
    for value in Comments.objects.order_by('-created_add').all():
        dict_list_comments.append(value.to_dict())
    return HttpResponse(json.dumps(dict_list_comments))


