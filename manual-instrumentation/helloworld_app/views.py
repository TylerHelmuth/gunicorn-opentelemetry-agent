from django.shortcuts import render

from django.http import HttpResponse

import logging

from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def hello_world(request):
    print("hello, world!")

    logging.getLogger().error("hello, error!")

    with tracer.start_as_current_span("test"):
        logging.getLogger().warning("hello, warn!")
        with tracer.start_as_current_span("test2") as test2:
            test2.set_attribute("test", 1)
    
    return HttpResponse("Hello World!")
