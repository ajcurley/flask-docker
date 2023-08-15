wsgi_app = "src.flask_docker.app:app"
bind = "0.0.0.0:8000"
workers = 4
accesslog = "-"
