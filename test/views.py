from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def test_index(request):
    return HttpResponse('장고 테스트')
