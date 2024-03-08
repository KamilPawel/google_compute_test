from django.http import Http404
from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin


class AdminAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Check if the request path is for the Django admin
        if resolve(request.path_info).app_name == "admin":
            # Check if the user is authenticated
            if not request.user.is_authenticated:
                # Return 404 if the user is not authenticated
                raise Http404()
        # Proceed to the next middleware or view if not accessing admin or user is authenticated
        return None
