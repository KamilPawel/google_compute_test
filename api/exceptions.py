from django.http import Http404
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call DRF's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP 404 handling
    if isinstance(exc, Http404):
        # Delegate to Django's default 404 handler
        from django.views.defaults import page_not_found

        return page_not_found(context["request"], exc)

    return response
