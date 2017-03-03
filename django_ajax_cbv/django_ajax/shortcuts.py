"""Helper functions for django ajax."""
import json
from django.shortcuts import _get_queryset
from django.http import HttpResponse


class JsonNotFound(Exception):
    """Easy to understand naming conventions work best."""

    pass


# replacement for django.shortcuts.get_object_or_404()
# allows json to be returned with a 404 error
def get_object_or_json_404(klass, *args, **kwargs):
    """Get the object or return a 404 error."""
    queryset = _get_queryset(klass)

    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        raise JsonNotFound()


def render_to_json_response(context, **response_kwargs):
    """Return a JSON response, transforming 'context' to make the payload."""
    response_kwargs['content_type'] = 'application/json'
    return HttpResponse(convert_context_to_json(context), **response_kwargs)


def convert_context_to_json(context):
    """Convert the context dictionary into a JSON object. note: this is *EXTREMELY* naive; in reality, you'll need to do much more complex handling to ensure that arbitrary objects -- such as Django model instances or querysets -- can be serialized as JSON."""
    return json.dumps(context)
