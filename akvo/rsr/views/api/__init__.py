from django.http import HttpResponse
import simplejson as json


class JsonResponse(HttpResponse):
    """django.http.HttpResponse object which accepts a native Python object
    and returns an HTTP response with JSON body and appropriate headers.
    """
    def __init__(self, content, content_type="application/json", **kwargs):
        self.content = json.dumps(content)
        self.content_type = content_type
