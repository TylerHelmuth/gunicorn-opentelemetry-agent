# Instructions

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install opentelemetry-distro
opentelemetry-bootstrap -a install
export DJANGO_SETTINGS_MODULE="helloworld_project.settings"
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
opentelemetry-instrument --traces_exporter console --metrics_exporter none --logs_exporter console --service_name testing gunicorn helloworld_project.wsgi -c gunicorn.conf.py --preload
```



