from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect

class LoginRequiredMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.path != '/accounts/login/','/Ganspa/register/' and not request.user.is_authenticated:
            return HttpResponseRedirect('/accounts/login/')
        return response