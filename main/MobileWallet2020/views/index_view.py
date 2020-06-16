from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from response import Response


def index_view(request):
    return render_to_response('index.html')
