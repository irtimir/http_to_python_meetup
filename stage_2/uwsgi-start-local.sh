#!/bin/bash
uwsgi --chdir ./src --module wsgi:application --http-socket 0.0.0.0:9090 --honour-stdin --workers 1 --enable-threads