# HTTP to python examples

## Requirements

* **docker**
* **docker compose**
* **python >3.6** for local run

## Stage 1

Serve static files with nginx.

### Common scheme

![stage 1 scheme](https://github.com/irtimir/http_to_python_meetup/blob/master/docs_static/stage_1_scheme.png?raw=true)

### Run

```shell
cd stage_1
docker compose up --build
```

## Stage 2

Connecting a minimal wsgi app to `gunicorn` and `uwsgi` and reverse proxy with `nginx`.

### Common scheme

![stage 2 scheme](https://github.com/irtimir/http_to_python_meetup/blob/master/docs_static/stage_2_scheme.png?raw=true)

### Run

```shell
cd stage_2
docker compose up --build
```

## Stage 3

Connecting a django app to `gunicorn` and serving static files with `nginx`.

### Common scheme

![stage 3 scheme](https://github.com/irtimir/http_to_python_meetup/blob/master/docs_static/stage_3_scheme.png?raw=true)

### Run

```shell
cd stage_3
docker compose up --build
```
