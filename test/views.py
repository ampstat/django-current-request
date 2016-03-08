from django.http import HttpResponse

import json

from djangocurrentrequest.middleware import get_current_request

def index(request):
    rq = get_current_request()
    return HttpResponse(json.dumps(
        dict(path=rq.path,
             server_name=rq.META.get('SERVER_NAME'))),
        content_type="application/json")
