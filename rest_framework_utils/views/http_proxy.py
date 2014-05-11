from django.http import HttpResponse
import requests
from django.http.response import HttpResponseNotAllowed, HttpResponseBadRequest


def proxy_to(request, path, target_url, modifier_fn=None):
    """
    Proxy to use cross domain Ajax GET and POST requests
    request: Django request object
    """
    url = '%s%s' % (target_url, path)

    if request.method == 'GET':
        request = request.GET
        r = requests.get
    elif request.method == 'POST':
        request = request.POST
        r = requests.post
    else:
        return HttpResponseNotAllowed("Permitted methods are GET")

    params = request.dict()
    response = r(url, params=params)
    res  = HttpResponse(response.text, status=int(response.status_code), mimetype=response.headers['content-type'])
    if modifier_fn:
        res = modifier_fn(res)
    return res
