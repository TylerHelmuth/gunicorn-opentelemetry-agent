from django.shortcuts import render

from django.http import HttpResponse

import logging

from opentelemetry import trace

tracer = trace.get_tracer(__name__)
logger = logging.getLogger(__name__)

def hello_world(request):
    print("hello, world!")

    logger.error("error no call to getLogger", extra={"foo": "bar"})
    logger.info("hello, info!")

    with tracer.start_as_current_span("test"):
        logger.warning("hello, warn!")
        logger.info("hello, info 2!")
        with tracer.start_as_current_span("test2") as test2:
            test2.set_attribute("test", 1)
    
    return HttpResponse("Hello World!")
