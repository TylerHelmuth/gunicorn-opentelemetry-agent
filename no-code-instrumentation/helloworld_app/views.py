from django.shortcuts import render

from django.http import HttpResponse

import logging

def hello_world(request):
    print("hello, world!")

    logging.getLogger().error("hello, error!")
    
    return HttpResponse("Hello World!")
