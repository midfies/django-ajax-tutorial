"""Middleware for django ajax custom exceptions."""
# from django.utils import timezone
# from django.utils.dateformat import format
# from django_ajax.exceptions import JsonNotFound
# from django_ajax.shortcuts import render_to_json_response


# class ExceptionMiddleware(object):
#     """To add custom exceptions."""

#     def process_exception(self, request, exception):
#         """Process the exception."""
#         if type(exception) == JsonNotFound:
#             now = format(timezone.now(), u'U')
#             kwargs = {}
#             response = {
#                 'status': '404',
#                 'message': 'Record not found',
#                 'timestamp': now,
#             }
#             return render_to_json_response(response, status=404, **kwargs)
#         return None
