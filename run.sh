#!/bin/bash

# run_app.sh

if [ "$1" == "gunicorn" ]; then
    echo "Running app using Gunicorn..."
    gunicorn helloworld_project.wsgi
elif [ "$1" == "dev" ]; then
    echo "Running app using Django development server..."
    python3 manage.py runserver
elif [ "$1" == "opentelemetry" ]; then
    echo "Running opentelemetry agent..."
    export OTEL_SERVICE_NAME=test-gunicorn
    export OTEL_TRACES_EXPORTER=otlp
    export OTEL_METRICS_EXPORTER=none 
    export OTEL_EXPORTER_OTLP_HEADERS="x-honeycomb-team=$HONEYCOMB_API_KEY"
    export OTEL_EXPORTER_OTLP_ENDPOINT=https://api.honeycomb.io
    export DJANGO_SETTINGS_MODULE="helloworld_project.settings"

    opentelemetry-instrument gunicorn helloworld_project.wsgi
else
    echo "Invalid argument. Use 'dev' to run the Django development server or 'gunicorn' to run the app using Gunicorn or 'opentelemetry' to run the app using Gunicorn with OpenTelemetry instrumentation."
    exit 1
fi
