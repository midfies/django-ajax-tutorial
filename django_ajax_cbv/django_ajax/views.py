"""The classes for django-ajax updating."""
from django.views.generic import UpdateView
from django_ajax.forms import UpdatePostForm
from django_ajax.shortcuts import get_object_or_json_404
from django_ajax.shortcuts import render_to_json_response
from django_ajax.models import Post


# a mixin to add AJAX support to a form
# must be used with an object-based FormView (e.g. CreateView)
class AjaxFormResponseMixin(object):
    """A mixin to replace form valid and invalid responses to JSON."""

    def form_invalid(self, form):
        """Return JSON response status 400."""
        return render_to_json_response(form.errors, status=400)

    def form_valid(self, form):
        """Return the object as JSON."""
        # save
        self.object = form.save()

        # initialize an empty context
        context = {}

        # return the context as json
        return render_to_json_response(self.get_context_data(context))


class AjaxPostUpdateView(AjaxFormResponseMixin, UpdateView):
    """The ajax post update view."""

    form_class = UpdatePostForm
    template_name = 'ajax_posts/post.html'

    def get_object(self, queryset=None):
        """Get the object or the 404 in JSON of the post."""
        # import pdb; pdb.set_trace()
        return get_object_or_json_404(Post, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        """."""
        context = super(AjaxPostUpdateView, self).get_context_data(**kwargs)
        context['success'] = True

        return context
