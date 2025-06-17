# Instructions

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export DJANGO_SETTINGS_MODULE="helloworld_project.settings"
export OTEL_EXPORTER_OTLP_HEADERS="x-honeycomb-team=your-key"
export OTEL_EXPORTER_OTLP_ENDPOINT="https://api.honeycomb.io:443"
gunicorn helloworld_project.wsgi -c gunicorn.conf.py --preload
```
