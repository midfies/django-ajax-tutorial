"""A form for updating posts."""
from django import forms
from django.forms import ModelForm
from django_ajax.models import Post


class UpdatePostForm(ModelForm):
    """Update a post."""

    name = forms.CharField(
        max_length=Post._meta.get_field('content').max_length
    )

    def save(self, commit=True):
        """Save the post."""
        instance = super(UpdatePostForm, self).save(commit=False)

        if commit:

            # save
            instance.save(update_fields=['name'])

        return instance

    class Meta:
        """Will still update all fields when saving the model."""

        model = Post
        fields = ('name',)
