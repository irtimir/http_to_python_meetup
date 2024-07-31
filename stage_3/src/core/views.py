import random

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse


def test_view(request: WSGIRequest) -> HttpResponse:
    print(type(request))
    print(request.environ)
    return HttpResponse(content=str(random.randint(0, 100)).encode())
