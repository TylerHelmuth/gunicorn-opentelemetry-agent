# Hello World Django Web App

This is a simple Django web app that returns "Hello World" when you visit the `/hello/` endpoint. The app is served using Gunicorn.

## Prerequisites

- Python 3 (tested on Python 3.8)
- Pip (Python package manager)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/helloworld_project.git
cd helloworld_project
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate # For Unix systems
venv\Scripts\activate # For Windows systems
```


3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the App Locally

1. Start the Django development server:

```bash
python manage.py runserver
```

2. Visit http://127.0.0.1:8000/hello/ in your web browser to see the "Hello World!" message.

3. Press `Ctrl + C` to stop the development server.

## Running the App with Gunicorn

1. Run the app using Gunicorn:

```bash
gunicorn helloworld_project.wsgi
```

2. Visit http://127.0.0.1:8000/hello/ in your web browser to see the "Hello World!" message.

3. Press `Ctrl + C` to stop Gunicorn.

## Running the App with OpenTelemetry

1. Install the opentelemetry agent

```bash
pip install opentelemetry-distro \
	opentelemetry-exporter-otlp

opentelemetry-bootstrap -a install
```

2. Run the app using Gunicorn + agent:

```bash
export OTEL_SERVICE_NAME=test-gunicorn
export OTEL_TRACES_EXPORTER=otlp
export OTEL_METRICS_EXPORTER=none 
export OTEL_EXPORTER_OTLP_HEADERS="x-honeycomb-team=$HONEYCOMB_API_KEY"
export OTEL_EXPORTER_OTLP_ENDPOINT=https://api.honeycomb.io

opentelemetry-instrument gunicorn helloworld_project.wsgi
```

3. Visit http://127.0.0.1:8000/hello/ in your web browser to see the "Hello World!" message.

4. Press `Ctrl + C` to stop Gunicorn.


## Deployment Notes

When deploying this app in a production environment, consider using a reverse proxy server (e.g., Nginx) to handle client requests and serve static files efficiently.

Please refer to the official Django documentation for more information on deploying Django apps:

- [Deploying Django](https://docs.djangoproject.com/en/3.2/howto/deployment/)
