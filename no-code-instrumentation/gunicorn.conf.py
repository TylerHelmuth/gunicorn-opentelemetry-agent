# from opentelemetry.sdk.resources import Resource

# import logging
# from opentelemetry._logs import set_logger_provider
# from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
# from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
# from opentelemetry.sdk._logs.export import ConsoleLogExporter

# from opentelemetry import trace
# from opentelemetry.sdk.trace.export import ConsoleSpanExporter
# from opentelemetry.sdk.trace import TracerProvider
# from opentelemetry.sdk.trace.export import BatchSpanProcessor

bind = "127.0.0.1:8000"

# Sample Worker processes
workers = 1
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2
