from django.http import HttpResponse
class HttpResponseMixin(object):
    def render_to_http_response(self,json_data):
        #1000 line of code
        return HttpResponse(json_data,content_type='application/json')
