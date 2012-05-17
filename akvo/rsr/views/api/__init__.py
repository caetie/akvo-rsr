from django.http import HttpResponse
import simplejson as json


class JsonResponse(HttpResponse):
    def __init__(self, content, content_type="application/json", **kwargs):
        self.content = json.dumps(content)
        self.content_type = content_type
