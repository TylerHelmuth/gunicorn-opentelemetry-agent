from opentelemetry.sdk.resources import Resource

import logging
from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

bind = "127.0.0.1:8000"

# Sample Worker processes
workers = 1
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)

    resource = Resource.create(
        attributes={
            "service.name": "testing",
            "worker": worker.pid,
        }
    )

    trace.set_tracer_provider(TracerProvider(resource=resource))
    span_processor = BatchSpanProcessor(
        OTLPSpanExporter()
    )
    trace.get_tracer_provider().add_span_processor(span_processor)

    logger_provider = LoggerProvider(resource)
    set_logger_provider(logger_provider)
    
    log_processor = BatchLogRecordProcessor(
        OTLPLogExporter()
    )
    logger_provider.add_log_record_processor(log_processor)
    handler = LoggingHandler(logger_provider=logger_provider)
    logging.getLogger().addHandler(handler)
