wsgi_app = 'config.wsgi:application'
bind = '0.0.0.0:9090'
workers = 5
threads = 2
# Restart workers when code changes.
# reload = True
