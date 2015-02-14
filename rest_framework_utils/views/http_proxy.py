from django.http import HttpResponse
import requests
from django.http.response import HttpResponseNotAllowed, HttpResponseBadRequest


def proxy_to(request, path, target_url, modifier_fn=None):
    """
    Proxy to use cross domain Ajax GET and POST requests
    request: Django request object
    """
    url = '%s%s' % (target_url, path)
    params = {}
    if request.method == 'GET':
        params = request.GET
        r = requests.get
    elif request.method == 'POST':
        params = request.POST
        r = requests.post
    else:
        return HttpResponseNotAllowed("Permitted methods are GET")

    response = r(url, params=params)
    res  = HttpResponse(response.text, status=int(response.status_code), content_type=response.headers['content-type'])
    if modifier_fn:
        res = modifier_fn(res, request, path)
    return res
